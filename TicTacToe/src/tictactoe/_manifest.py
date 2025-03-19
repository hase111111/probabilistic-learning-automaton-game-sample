"""
# Copyright (c) 2025 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

_manifest.py

This file is used to hide the pygame support prompt
    that is displayed when the pygame module is imported.
"""

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
