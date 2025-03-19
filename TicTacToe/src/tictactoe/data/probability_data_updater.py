"""
# Copyright (c) 2025 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

probability_data_updater.py

"""


class ProbabilityDataUpdater:
    def __init__(self):
        self.alpha = 0.1  # learning rate

    def update(self, data: dict, battle_log: list, mark: str, winner: str):
        """
        バトルログから勝者の情報をもとに確率データを更新する．
        """
        if winner == "draw":
            return self._update_draw(data, battle_log)
        elif winner == mark:
            return self._update_win(data, battle_log)
        else:
            return self._update_lose(data, battle_log)

    def _update_draw(self, data: dict, battle_log: list):
        """
        引き分けの場合の確率データの更新．
        """
        alpha = self.alpha / 2
        for field, move in battle_log:
            for key in data[field]:
                if key == move:
                    data[field][key] = (1 - alpha) * data[field][key] + alpha * 100
                else:
                    data[field][key] = (1 - alpha) * data[field][key]
        return data

    def _update_win(self, data: dict, battle_log: list):
        """
        勝利した場合の確率データの更新．
        """
        alpha = self.alpha
        for field, move in battle_log:
            for key in data[field]:
                if key == move:
                    data[field][key] = (1 - alpha) * data[field][key] + alpha * 100
                else:
                    data[field][key] = (1 - alpha) * data[field][key]
        return data

    def _update_lose(self, data: dict, battle_log: list):
        """
        敗北した場合の確率データの更新．
        """
        return data
        alpha = self.alpha
        for field, move in battle_log:
            for key in data[field]:
                if key != move:
                    data[field][key] = (1 - alpha) * data[field][key] + alpha * 100
                else:
                    data[field][key] = (1 - alpha) * data[field][key]
        return data
