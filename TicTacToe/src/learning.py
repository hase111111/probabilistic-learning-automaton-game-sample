"""learning.py"""

import json

import tictactoe.data
import tictactoe.battle


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


def main2():
    gene = tictactoe.data.BoardEnumerator()
    boards = gene.get_all_boards()

    dict_boards = dict()
    for _, board in enumerate(boards):
        f = tictactoe.data.Field()
        f.from_data(board)
        move = f.get_all_available_moves()
        move_dict = dict()
        for m in move:
            move_dict[m] = 100 / len(move)
        dict_boards[board] = move_dict

    player1 = tictactoe.battle.RandomAgent()
    player2 = tictactoe.battle.RandomAgent()
    battle = tictactoe.battle.BattleSequence(player1, player2, print_flag=False)

    print(dict_boards["x-x-o----"])
    alpha = 0.1  # learning rate

    for _ in range(10):
        battle.play()

        # if O wins, reward O
        if battle.battle_result == "o":
            for data, move in battle.battle_log:
                dict_boards[data][move] += 10

    print(dict_boards["---------"])


if __name__ == "__main__":
    main2()
