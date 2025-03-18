"""learning.py"""

import json

import tictactoe.data


def main():
    gene = tictactoe.data.BoardEnumerator()
    boards = gene.get_all_boards()

    dict_boards = dict()
    for i, board in enumerate(boards):
        f = tictactoe.data.Field()
        f.from_data(board)
        move = f.get_all_available_moves()
        move_dict = dict()
        for m in move:
            move_dict[m] = 100 / len(move)
        dict_boards[board] = move_dict

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(dict_boards, f)


if __name__ == "__main__":
    main()
