"""field.py"""

BLANK = " "
CROSS = "x"
ZERO = "o"
FIELD_SIZE = 3


class Field:
    """
    This class represents the field of the game.
    """

    def __init__(self):
        self.field = [[BLANK for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

    def __str__(self):
        return "\n".join([" | ".join(row) for row in self.field])

    def __getitem__(self, key):
        return self.field[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            # if key is a tuple
            self.field[key[0]][key[1]] = value
        else:
            # if key is a single value
            row = key // FIELD_SIZE
            col = key % FIELD_SIZE
            self.field[row][col] = value

    def get_all_available_moves(self):
        """
        Get all available moves in the field.
        """
        return [
            i
            for i in range(FIELD_SIZE**2)
            if self.field[i // FIELD_SIZE][i % FIELD_SIZE] == BLANK
        ]

    def to_data(self) -> str:
        """
        convert the field to a string.

        o |   | x
        x | o | x  => o-xxoxxoo
        x | o | o
        """
        ans = ""
        for row in self.field:
            for cell in row:
                ans += cell if cell != BLANK else "-"
        return ans

    def from_data(self, data: str):
        """
        convert the string to the field.
        """

        for i, cell in enumerate(data):
            row = i // FIELD_SIZE
            col = i % FIELD_SIZE
            self.field[row][col] = cell if cell != "-" else BLANK

    def is_winner(self, player) -> bool:
        """
        Check if the player has won the game.

        Args:
            player (str): The player to check for. "o" or "x".
        """

        for row in self.field:
            if all([cell == player for cell in row]):
                return True

        for col in range(FIELD_SIZE):
            if all([self.field[row][col] == player for row in range(FIELD_SIZE)]):
                return True

        if all([self.field[i][i] == player for i in range(FIELD_SIZE)]):
            return True

        if all([self.field[i][2 - i] == player for i in range(FIELD_SIZE)]):
            return True

        return False
