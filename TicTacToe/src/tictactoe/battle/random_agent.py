"""
# Copyright (c) 2025 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

random_agent.py

"""

import random

from ..data.field import Field


class RandomAgent:
    def get_action(self, field: Field) -> int:
        return random.choice(field.get_all_available_moves())
