class UIException(Exception):
    pass


class UI:
    def __init__(self, game):
        self._game = game

    @staticmethod
    def read_human_move():
        move = input("What is your next move? (Type X to exit)")
        if move.lower() == 'x':
            return -1, -1

        if len(move) < 2:
            raise UIException("Invalid move!")

        col = move[0].lower()
        row = move[1:]

        col_ind = ord(col) - 97
        try:
            row_ind = int(row) - 1
        except ValueError as error:
            raise UIException("The position is invalid!")

        return row_ind, col_ind

    def run(self):
        human_turn = None
        human_first = None
        done = False

        while not done:
            answer = input("Do you want to play first? (Yes/No)\n")
            if answer.lower() == "yes":
                human_turn = True
                human_first = True
                done = True
            elif answer.lower() == "no":
                human_turn = False
                human_first = False
                done = True
            else:
                print("Invalid answer!")

        done = False

        while not done:
            try:
                print(self._game.board)

                if human_turn is True:
                    move = self.read_human_move()

                    if move[0] == -1 and move[1] == -1:
                        done = True
                        break

                    if self._game.human_move(*move, human_first) is True:
                        done = True
                        print("You won!")
                        print(self._game.board)

                        continue
                else:
                    print("Waiting for computer's turn...")
                    if self._game.computer_move(not human_first)[0] is True:
                        done = True
                        print("I won!")
                        print(self._game.board)

                        continue

                if self._game.is_draw():
                    print("It's a draw!")
                    done = True

                human_turn = not human_turn
            except Exception as error:
                print(error)
