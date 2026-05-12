import logging
import time
from pathlib import Path
from typing import Dict, Any, Optional

from playwright.sync_api import Page, Response

from ..itf_api_interceptor import IApiInterceptor
from ..itf_client import IWebDriverClient

_PROJECT_ID_FILE = Path("/tmp/project_id.txt")


class PlaywrightApiInterceptor(IApiInterceptor):

    def __init__(self, driver: IWebDriverClient):
        self._driver = driver
        self._captured_responses: Dict[str, Dict[str, Any]] = {}
        self._setup_response_interception()

    def _get_page(self) -> Page:
        return self._driver._page

    def wait_for_response_with_url(self, url_pattern: str, timeout: int = 30) -> Optional[Dict[str, Any]]:
        """
        Wait for a response that matches the URL pattern and capture it.

        Args:
            url_pattern: Pattern to match in the URL (substring match)
            timeout: Maximum time to wait in seconds

        Returns:
            Dict with response data or None if timeout
        """
        try:
            logging.info(f"Waiting for response matching pattern: {url_pattern}")
            with self._get_page().expect_response(
                lambda response: url_pattern in response.url,
                timeout=timeout * 1000
            ) as response_info:
                pass

            response = response_info.value
            response_data = self.capture_response(response)
            logging.info(f"Captured response for URL: {response.url}")
            return response_data

        except Exception as e:
            logging.error(f"Timeout waiting for response with pattern '{ url_pattern}': {e}")
            return None

    def capture_response(self, response: Response) -> Dict[str, Any]:
        """
        Extract relevant data from a Playwright Response object and store it.

        Args:
            response: Playwright Response object

        Returns:
            Dict with response data
        """
        request_headers = dict(response.request.headers)
        response_data = {
            "url": response.url,
            "status": response.status,
            "status_text": response.status_text,
            "headers": dict(response.headers),
            "request_headers": request_headers,
            "ok": response.ok,
            "timestamp": time.time()
        }

        # Try to capture response body
        try:
            content_type = response.headers.get("content-type", "")

            if "application/json" in content_type:
                response_data["body"] = response.json()
                response_data["body_type"] = "json"
            else:
                # For non-JSON responses, store as text
                body_text = response.text()
                response_data["body"] = body_text if len(body_text) < 10000 else body_text[:10000] + "... [truncated]"
                response_data["body_type"] = "text"

        except Exception as e:
            logging.debug(f"Could not capture response body from {response.url}: {e}")
            response_data["body"] = None
            response_data["body_type"] = "error"
            response_data["body_error"] = str(e)

        self._captured_responses[response.url] = response_data
        return response_data

    def get_captured_response(self, url_pattern: str) -> Optional[Dict[str, Any]]:
        """ Get the most recent captured response that matches the URL pattern. """
        for url, response_data in reversed(list(self._captured_responses.items())):
            if url_pattern in url:
                logging.info(f"Found captured response for pattern '{url_pattern}': {url}")
                return response_data
        logging.warning(f"No captured response found for pattern: {url_pattern}")
        return None

    def get_all_captured_responses(self) -> Dict[str, Dict[str, Any]]:
        """ Get all captured responses. """
        return self._captured_responses.copy()

    def clear_captured_responses(self):
        """Clear all captured responses."""
        logging.debug("Clearing all captured responses")
        self._captured_responses.clear()

    def _setup_response_interception(self):
        """Set up response listener to capture API responses."""
        def handle_response(response):
            try:
                # Check for Project-Id header on ANY request, before any other filter
                if not _PROJECT_ID_FILE.exists():
                    project_id = response.request.headers.get("project-id")
                    if project_id:
                        _PROJECT_ID_FILE.write_text(project_id)
                        logging.info(f"[API] Captured Project-Id and saved to {_PROJECT_ID_FILE}: {project_id}")

                # Filter out non-HTTP API requests (static resources, etc.)
                if not self._should_capture_response(response):
                    return

                # Capture the response data
                self.capture_response(response)

                # Log with improved format
                endpoint = self._extract_endpoint_path(response.url)
                method = response.request.method
                status = response.status
                status_symbol = "✓" if 200 <= status < 300 else "✗" if status >= 400 else "●"

                logging.info(f"[API] {status_symbol} {method} {endpoint} → {status}")
            except Exception as e:
                logging.debug(f"Could not capture response from {response.url}: {e}")

        self._get_page().on("response", handle_response)
        logging.info("Response interception enabled for API calls")

    def _extract_endpoint_path(self, url: str) -> str:
        """
        Extract a clean endpoint path from a full URL for logging.
        """
        try:
            from urllib.parse import urlparse
            parsed = urlparse(url)
            path = parsed.path

            # Include query params for better context
            if parsed.query:
                # Simplify query params for readability
                query_parts = parsed.query.split('&')
                if len(query_parts) > 2:
                    query = f"?{query_parts[0]}&...({len(query_parts)-1} more)"
                else:
                    query = f"?{parsed.query}"
                return f"{path}{query}"

            return path
        except Exception:
            return url

    def _should_capture_response(self, response) -> bool:
        """
        Determine if a response should be captured based on custom criteria.
        Only captures HTTP API calls, not static resources or framework requests.
        """
        url = response.url.lower()

        # Exclude static resources (JS, CSS, images, fonts, etc.)
        static_extensions = [
            '.js', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico',
            '.woff', '.woff2', '.ttf', '.eot', '.map', '.webp', '.mp4', '.webm'
        ]
        if any(url.endswith(ext) for ext in static_extensions):
            return False

        # Exclude common static resource paths
        static_paths = [
            '/_next/static/',
            '/static/',
            '/assets/',
            '/images/',
            '/fonts/',
            '/favicon',
            '/__nextjs',
            '/_next/webpack'
        ]
        if any(path in url for path in static_paths):
            return False

        # Exclude Next.js framework requests (React Server Components, prefetch, etc.)
        # These include query params like _rsc, _next_data, etc.
        framework_query_params = ['_rsc=', '_next_data=', '__next']
        if any(param in url for param in framework_query_params):
            return False

        # Only capture responses with application/json content-type
        content_type = response.headers.get("content-type", "")
        is_json = "application/json" in content_type

        # Exclude text/x-component and other non-JSON content types
        if any(ct in content_type for ct in ["text/x-component", "text/html", "text/plain"]):
            return False

        # Define API endpoint patterns to capture (must also have JSON content-type)
        api_patterns = [
            "/customer",
            "/projects",
            "/workspace",
            "/datasource",
            "/datasources",
            "/usage",
            "/engagement"
        ]

        has_api_pattern = any(pattern in url for pattern in api_patterns)

        # IMPORTANT: Only capture if it's JSON AND matches API patterns
        # This prevents capturing framework requests that happen to match patterns
        return is_json and has_api_pattern