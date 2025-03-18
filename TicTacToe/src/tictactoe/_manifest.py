"""
This file is used to hide the pygame support prompt
    that is displayed when the pygame module is imported.
"""

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
