import random

from ..data.field import Field


class RandomAgent:
    def get_action(self, field: Field) -> int:
        return random.choice(field.get_all_available_moves())
