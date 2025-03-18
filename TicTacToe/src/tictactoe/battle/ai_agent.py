import random

from ..data.field import Field


class AiAgent:
    def __init__(self, study_data: dict, use_best_move: bool = False):
        self.study_data: dict = study_data
        self.use_best_move = use_best_move

    def get_action(self, field: Field) -> int:
        field_str = field.to_data()
        move_dict = self.study_data[field_str]

        if self.use_best_move:
            return self._choice_best_move(move_dict)

        return self._choice(move_dict)

    def _choice_best_move(self, move_dict: dict) -> int:
        """
        数字と重みづけ係数の辞書を受け取り、数字を返す．
        この時，重みづけ係数(float)に基づいて選択する．
        """

        # 重みづけ係数が最大のものを選択
        max_ = 0
        ret = 0
        for key, value in move_dict.items():
            if value > max_:
                max_ = value
                ret = key

        return ret

    def _choice(self, move_dict: dict) -> int:
        """
        数字と重みづけ係数の辞書を受け取り、数字を返す．
        この時，重みづけ係数(float)に基づいて選択する．
        """

        # 重みづけ係数の合計を計算
        sum_ = 0
        for key in move_dict:
            sum_ += move_dict[key]

        # 重みづけ係数に基づいて選択
        r = random.random() * sum_
        key = None
        for key in move_dict:
            r -= move_dict[key]
            if r < 0:
                break

        return key
