import json

from .field import Field
from .board_enumerator import BoardEnumerator


class ProbabilityData:
    def __init__(self):
        self.data = {}

    def __str__(self):
        ret = ""
        for key, value in self.data.items():
            ret += f"{key} : {value}\n"
        return ret

    def initialize(self):
        gene = BoardEnumerator()
        boards = gene.get_all_boards()

        self.data = {}
        for _, board in enumerate(boards):
            f = Field()
            f.from_data(board)
            move = f.get_all_available_moves()
            move_dict = {}
            for m in move:
                move_dict[m] = 100 / len(move)
            self.data[board] = move_dict

    def save(self, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f)

    def load(self, filename: str):
        with open(filename, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_raw_data(self):
        return self.data
