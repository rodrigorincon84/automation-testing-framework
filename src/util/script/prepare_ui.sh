#!/bin/bash
set -euo pipefail

VERSION_ALIAS="current_downloaded"
DEFAULT_CHROME_VERSION="148.0.7778.97"
CHROME_VERSION="${1:-$DEFAULT_CHROME_VERSION}"
PROJECT_ROOT="${PROJECT_PATH:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)}"
BASE_DIR="${PROJECT_ROOT}/.local/tool"

OS="$(uname -s)"
ARCH="$(uname -m)"

if [[ "$OS" == "Linux" && "$ARCH" == "x86_64" ]]; then
  PLATFORM="linux64"
elif [[ "$OS" == "Darwin" && "$ARCH" == "arm64" ]]; then
  PLATFORM="mac-arm64"
elif [[ "$OS" == "Darwin" && "$ARCH" == "x86_64" ]]; then
  PLATFORM="mac-x64"
else
  echo "❌ Unsupported platform: OS=$OS ARCH=$ARCH"
  exit 1
fi

echo "🖥 Detected platform: $PLATFORM"

TARGET_DIR="${BASE_DIR}/${CHROME_VERSION}/${PLATFORM}"

# Check if browsers already exist (from cache)
if [[ -d "$TARGET_DIR" ]] && [[ -f "${TARGET_DIR}/chromedriver" ]]; then
  echo "Browsers already exist (version: $CHROME_VERSION)"
  echo "   Chrome path: ${TARGET_DIR}/chrome"
  echo "   Chromedriver: ${TARGET_DIR}/chromedriver"

  # Update symlink
  ln -sf "${BASE_DIR}/${CHROME_VERSION}" "${BASE_DIR}/${VERSION_ALIAS}"

  echo "Skipping download (using cached browsers)"
  exit 0
fi

# If not cached, proceed with download
echo "Browsers not found in cache. Starting download..."

# Clean OLD versions only (not the current version)
echo "Cleaning old browser versions..."
find "$BASE_DIR" -mindepth 1 -maxdepth 1 -type d ! -name "$CHROME_VERSION" -exec rm -rf {} + 2>/dev/null || true

mkdir -p "$TARGET_DIR"
ln -sf "${BASE_DIR}/${CHROME_VERSION}" "${BASE_DIR}/${VERSION_ALIAS}"

BASE_URL="https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/${PLATFORM}"

### ───── Chrome ─────
CHROME_ZIP="chrome-${PLATFORM}.zip"
CHROME_TMP="/tmp/${CHROME_ZIP}"

echo "⬇️  Downloading Chrome from ${BASE_URL}/${CHROME_ZIP}"
curl -fsSL \
  --retry 5 \
  --retry-delay 2 \
  -o "$CHROME_TMP" \
  "${BASE_URL}/${CHROME_ZIP}"

echo "📦  Extracting Chrome..."
unzip -q "$CHROME_TMP" -d /tmp

if [[ "$PLATFORM" == "mac-arm64" ]] || [[ "$PLATFORM" == "mac-x64" ]]; then
  echo "🚚  Moving macOS .app to ${TARGET_DIR}/chrome.app"
  mv "/tmp/chrome-${PLATFORM}/Google Chrome for Testing.app" "${TARGET_DIR}/chrome.app"
else
  echo "🚚  Moving Linux chrome dir to ${TARGET_DIR}/chrome"
  mv "/tmp/chrome-${PLATFORM}" "${TARGET_DIR}/chrome"
fi

rm -f "$CHROME_TMP"

### ───── Chromedriver ─────
DRIVER_ZIP="chromedriver-${PLATFORM}.zip"
DRIVER_TMP="/tmp/${DRIVER_ZIP}"

echo "⬇️  Downloading Chromedriver from ${BASE_URL}/${DRIVER_ZIP}"
curl -# -L -o "$DRIVER_TMP" "${BASE_URL}/${DRIVER_ZIP}"

echo "📦  Extracting Chromedriver..."
unzip -q "$DRIVER_TMP" -d /tmp

echo "🚚  Moving chromedriver binary to ${TARGET_DIR}/chromedriver"
mv "/tmp/chromedriver-${PLATFORM}/chromedriver" "${TARGET_DIR}/chromedriver"
chmod +x "${TARGET_DIR}/chromedriver"

rm -f "$DRIVER_TMP"

# 🧹 Clean temp
rm -rf "/tmp/chrome-${PLATFORM}" "/tmp/chromedriver-${PLATFORM}"

echo "✅  Done: $PLATFORM (version: $CHROME_VERSION)"
echo "   Browsers cached in: $TARGET_DIR"