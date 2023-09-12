from Domain.Board import Board, BoardException
from Domain.Player import Player
from Game.Connect4 import Connect4


class Connect4UI:
    def __init__(self, strategy):
        # initial settings of the game:
        self._height = 6  # the board height
        self._width = 7  # the board width
        self._winning_pieces = 4  # the pieces required to win
        self._player1 = Player('h', 1, 'x')
        self._player2 = Player('c', 2, 'o')
        self._strategy = strategy  # the ai strategy used
        self._AI_intelligence = 4  # the ai intelligence (for the minimax strat, this is equivalent to the search
        # max_depth)

    @staticmethod
    def print_main_menu():
        """ Print the main menu """
        print("~~~~~~~~Connect 4~~~~~~~~")
        print("~~~~~~~~1 -  Play~~~~~~~~")
        print("~~~~~~~~2 - Settings~~~~~")
        print("~~~~~~~~3 - Quit~~~~~~~~~")

    def run_menu(self):
        """ Run the main menu """
        finished = False

        while not finished:
            self.print_main_menu()
            option = input("Enter an option: ")

            if option == '1':
                self.run_game()
            elif option == '2':
                self.run_settings()
            elif option == '3':
                finished = True
                print("Goodbye!")
            else:
                print("Invalid option")

    def print_settings(self):
        """ Print the settings menu """
        print("1 - Player 1: " + ('human' if self._player1.type == 'h' else 'computer'))
        print("2 - Player 2: " + ('human' if self._player2.type == 'h' else 'computer'))
        print("3 - AI intelligence: " + str(self._AI_intelligence))
        print("4 - Save")

    def run_settings(self):
        """ Run the settings menu """
        finished = False

        while not finished:
            self.print_settings()
            option = input("Enter an option: ")

            if option == '1' or option == '2':
                valid = False
                while not valid:
                    player_type = input("Enter a player type: ")
                    if player_type not in ('h', 'c'):
                        print("Invalid player type")
                    else:
                        if option == '1':
                            self._player1.type = player_type
                        else:
                            self._player2.type = player_type
                        valid = True
            elif option == '3':
                valid = False
                while not valid:
                    ai_intelligence = input("Enter a value from 1 to 7 (higher values are slower):")
                    try:
                        ai_intelligence = int(ai_intelligence)
                        if ai_intelligence < 1 or ai_intelligence > 7:
                            print("Intelligence must be a number between 1 and 6.")
                        else:
                            self._AI_intelligence = ai_intelligence
                            valid = True
                    except ValueError:
                        print("Invalid input.")
            elif option == '4':
                finished = True

    def print_board(self, board):
        """
        Print the board to the console
        :param board: the board instance to be printed
        :return: void
        """
        for row in range(board.height):
            board_row = ""
            for col in range(board.width):
                if board[row][col].is_empty():
                    board_row += '_ '
                elif board[row][col].value == 1:
                    board_row += self._player1.piece + ' '
                elif board[row][col].value == 2:
                    board_row += self._player2.piece + ' '
            print(board_row)
        print("_____________")
        print("0 1 2 3 4 5 6")

    @staticmethod
    def get_move_from_human():
        """ Query the human for their next move """
        while True:  # ask the user for input until it's valid
            try:
                move = input("Enter a column: ")
                return int(move)
            except ValueError:
                print("Invalid input, enter an integer from 0 to 6.")

    def run_game(self):
        """ Run the game """
        board = Board(self._height, self._width, self._winning_pieces)
        strategy = self._strategy(board, self._AI_intelligence)
        game = Connect4(board, strategy, self._player1, self._player2)
        game_over = False

        while not game_over:
            print('\n\n')
            self.print_board(board)

            if board.won():
                losing_player = game.get_current_player()  # the player who has the current turn lost

                if losing_player.id == 1:
                    print("Player 2 wins.\n\n")
                else:
                    print("Player 1 wins.\n\n")
                game_over = True
            elif board.is_full():
                print("Stalemate.\n\n")
                game_over = True
            else:
                current_player = game.get_current_player()

                if current_player.type == 'h':
                    while True:  # ask the player for a piece and try to place it until success
                        try:
                            move = self.get_move_from_human()
                            game.next_human_move(move)
                            break
                        except BoardException:
                            print("Invalid move")
                else:
                    game.next_computer_move()
