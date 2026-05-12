import os

from pyprojroot import here


class OS:

    WINDOWS = 'windows'
    LINUX = 'linux'
    MACOS = "darwin"
    ALPINE = "x86_64"


class System:

    PROJECT_PATH = os.getenv("PROJECT_ROOT", here())
