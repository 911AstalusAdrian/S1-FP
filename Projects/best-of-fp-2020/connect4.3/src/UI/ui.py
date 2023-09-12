from Strategy.strategy import *
from Game.game import *


class UI:
    def __init__(self):

        self._game = Game()

    def read_human_move(self):

        coord = input('where to play>')
        right=False

        while not right:
            if '1'<=coord<='7':
                if self._game.board.is_free(int(coord)-1):
                    row = int(coord)
                    return row - 1
                else:
                    print('That column is full!')
                    coord = input('where to play>')
            else:
                print('Wrong input!')
                coord = input('where to play>')

    def start(self):
        finished = False
        human_turn = True
        difficulty=int(input('Choose the difficulty where 1 is very easy and 5 is very hard:'))

        while not finished:
            # Print the board state
            if self._game.board.checkWin('O') is True:
                print('Computer wins!\n')
                print(self._game.board)
                return
            elif self._game.board.checkWin('X') is True:
                print('You win\n')
                print(self._game.board)
                return
            elif self._game.board.is_full() is True:
                print('Tie\n')
                print(self._game.board)
                return
            else:
                print(self._game.board)

            if human_turn:
                coord = self.read_human_move()

                if self._game.human_move(coord) is False:


                    return
            else:
                if self._game.computer_move(difficulty) is False:


                    return
            human_turn = not human_turn

#
# ui = UI()
# ui.start()