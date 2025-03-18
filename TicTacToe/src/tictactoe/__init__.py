"""__init__.py: This file is used to initialize the package tictactoe."""

from ._manifest import *

from .game_loop import GameLoop
from .data.field import Field, BLANK, CROSS, ZERO, FIELD_SIZE
