"""
# Copyright (c) 2025 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

learning.py

"""

import random

import tictactoe.data as td
import tictactoe.battle as tb


def main():
    pro1 = td.ProbabilityData()
    pro1.initialize()
    pro2 = td.ProbabilityData()
    pro2.initialize()

    player1 = tb.AiAgent(pro1.get_raw_data())
    player2 = tb.AiAgent(pro2.get_raw_data())
    battle = tb.BattleSequence(player1, player2, print_flag=False, first_player="o")
    updater = td.ProbabilityDataUpdater()

    for _ in range(10**5):
        battle.first_player = random.choice([td.ZERO, td.CROSS])
        battle.play()
        battle_log = battle.battle_log
        battle_result = battle.battle_result
        updater.update(pro1.get_raw_data(), battle_log, td.ZERO, battle_result)
        updater.update(pro2.get_raw_data(), battle_log, td.CROSS, battle_result)

    player1 = tb.AiAgent(pro1.get_raw_data(), use_best_move=True)
    player2 = tb.AiAgent(pro2.get_raw_data(), use_best_move=True)
    battle = tb.BattleSequence(player1, player2, print_flag=True, first_player="o")
    battle.play()

    battle.first_player = "x"
    battle.play()

    data = pro1.get_raw_data()
    print(data["---------"])
    data = pro2.get_raw_data()
    print(data["---------"])


if __name__ == "__main__":
    main()
