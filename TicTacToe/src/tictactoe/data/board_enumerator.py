"""
# Copyright (c) 2025 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

board_enumerator.py

"""

import copy

from .field import Field, CROSS, ZERO


class BoardEnumerator:
    """
    This class is responsible for enumerating all possible boards.
    """

    def get_all_boards(self):
        """
        Get all possible boards.
        """
        field_set = set()
        field_set.add(Field().to_data())

        # queue is tuple list of (field_str, player)
        queue = [(Field().to_data(), CROSS)]

        # BFS
        while queue:
            current_field, current_player = queue.pop(0)
            next_boards = self._generate_next_boards(current_field, current_player)
            for next_board in next_boards:
                if next_board not in field_set:
                    field_set.add(next_board)

                    # if each player is winning, then the board is not valid
                    f = Field()
                    f.from_data(next_board)
                    if f.is_winner(CROSS) or f.is_winner(ZERO):
                        continue
                    queue.append(
                        (next_board, CROSS if current_player == ZERO else ZERO)
                    )

        field_set = self._add_inv_data(field_set)

        return field_set

    def _generate_next_boards(self, field_str: str, player):
        """
        Generate all possible boards.

        Args:
            field (Field): The current field.
            player (str): The player to move. "o" or "x".
        """
        field = Field()
        field.from_data(field_str)
        next_boards = field.get_all_available_moves()

        ret = []

        for move in next_boards:
            new_field = copy.deepcopy(field)
            new_field[move] = player
            ret.append(new_field.to_data())

        return ret

    def _inv_data(self, data: str):
        """
        Return the inverse data of the given data.
        """
        ret = ""
        for cell in data:
            if cell == "x":
                ret += "o"
            elif cell == "o":
                ret += "x"
            else:
                ret += "-"
        return ret

    def _add_inv_data(self, data_set: set):
        """
        Add the inverse data of the given data to the set.
        """
        for data in list(data_set):
            data_set.add(self._inv_data(data))
        return data_set
