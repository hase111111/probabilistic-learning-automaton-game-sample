import random

from ..data.field import Field


class AiAgent:
    def __init__(self, study_data: dict, *, mark="o"):
        self.study_data: dict = study_data
        self.mark: str = mark

    def get_action(self, field: Field) -> int:
        field_str = field.to_data()
        if self.mark == "x":
            field_str = self._inv_data(field_str)
        move_dict = self.study_data[field_str]
        return self._choice(move_dict)

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
        r = random.random()
        key = None
        for key in move_dict:
            r -= move_dict[key] / sum_
            if r < 0:
                break

        return key

    def _inv_data(self, data: str) -> str:
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
