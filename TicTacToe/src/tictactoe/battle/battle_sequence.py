from ..data import Field, ZERO, CROSS


class BattleSequence:
    def __init__(self, player1, player2, *, first_player=ZERO, print_flag=True):
        self.player1 = player1
        self.player2 = player2
        self.field = Field()
        self.first_player = first_player
        self.turn = first_player
        self.battle_log = []
        self.battle_result = "yet"
        self.print_flag = print_flag

    def play(self):
        self._reset()
        while not self._end_game():
            move = (
                self.player1.get_action(self.field)
                if self.turn == ZERO
                else self.player2.get_action(self.field)
            )
            self.battle_log.append((self.field.to_data(), move))
            self.field[move] = self.turn
            self._switch_turn()

            self._print_field()

        self._set_battle_result()
        self._print_result()

    def _end_game(self):
        return (
            self.field.is_winner(ZERO)
            or self.field.is_winner(CROSS)
            or self.field.get_all_available_moves() == []
        )

    def _switch_turn(self):
        self.turn = ZERO if self.turn == CROSS else CROSS

    def _set_battle_result(self):
        if self.field.is_winner(ZERO):
            self.battle_result = ZERO
        elif self.field.is_winner(CROSS):
            self.battle_result = CROSS
        else:
            self.battle_result = "draw"

    def _print_field(self):
        if not self.print_flag:
            return
        print("=" * 10)
        print(self.field)
        print()

    def _print_result(self):
        if not self.print_flag:
            return
        print("Result")
        print("=" * 10)

        if self.field.is_winner(ZERO):
            print(f"Winner: {ZERO}")
        elif self.field.is_winner(CROSS):
            print(f"Winner: {CROSS}")
        else:
            print("Draw")
        print(self.field)
        print("=" * 10)

    def _reset(self):
        self.field = Field()
        self.turn = self.first_player
        self.battle_log = []
        self.battle_result = "yet"
