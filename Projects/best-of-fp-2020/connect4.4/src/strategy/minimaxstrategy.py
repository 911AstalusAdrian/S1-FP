import math
from copy import copy

from board.cell import Cell
from strategy.strategy import Strategy
from utility.gameutility import GameCalculations


class MinimaxStrategy(Strategy):
    MINIMAX_DEPTH = 3
    WINNING = 100000000
    FOUR_IN_A_ROW_SCORE = 10000
    THREE_IN_A_ROW_SCORE = 9
    TWO_IN_A_ROW_SCORE = 4
    ONE_IN_A_ROW_SCORE = 1

    def move(self, board, value, enemy_value):
        """
        Does a move using the minimax strategy
        :param board: The board on which the game is played, an object of type Board
        :param value: The value used to represent the pieces of the player for which the method does the move
        :param enemy_value: The value used to represent the pieces of the opposing player
        :return: The new form of the Cell affected by the move, an object of type Cell
        """
        minimax_result = self.minimax(board, self.MINIMAX_DEPTH, value, enemy_value)
        if minimax_result[1] % MinimaxStrategy.WINNING == 0 and minimax_result[1] < 0:
            # This means that the opposing player will win no matter what we do, so we just try to block one of his ways
            # to win
            cell = self.generate_winning_move(board, enemy_value)
            if cell is not None:
                # If the enemy player can win in the next move, cell will not be None and we do that move for our player
                board.set_value(cell.line, cell.column, value)
                return Cell(cell.line, cell.column, value)
        # If the enemy player cannot win in the next move, we use the results of the minimax algorithm
        column = minimax_result[0]
        line = board.get_line_first_empty_cell_in_column(column)
        board.set_value(line, column, value)
        return Cell(line, column, value)

    def minimax(self, board, depth, value, enemy_value, alpha=-math.inf, beta=math.inf, maxi=True, last_move=None):
        """
        Calculates the ideal move using the minimax algorithm.
        :param board: The board on which the move is made, an object of type Board
        :param depth: The depth of the minimax search, an integer
        :param value: The value used to represent the pieces of the player for which the method does the move, the
        maximizing player
        :param enemy_value: The value used to represent the pieces of the opposing player, the minimizing player
        :param alpha: The minimum score that the maximizing player is assured to achieve. It is used in alpha-beta
        pruning, an optimization of the classic minimax algorithm. It is a float, and if not specified, it takes the
        value -infinity
        :param beta: The maximum score that the minimizing player is assured to achieve. It is used in alpha-beta
        pruning, an optimization of the classic minimax algorithm. It is a float, and if not specified, it takes the
        value infinity
        :param maxi: Whether or not the current player is the one that maximizes the score or not, a boolean
        :param last_move: The Cell affected by the last move done during the search, an object of type Cell
        :return: A tuple with two elements, the first being the column on which the best move is done on, and the second
        being the score achieved during the search
        """
        if last_move is not None and GameCalculations.is_winner(board, last_move):
            # If the last move decided the game in someone's favor, it is not necessary to search any further.
            if last_move.value == value:
                return None, MinimaxStrategy.WINNING * (depth + 1)
            return None, -MinimaxStrategy.WINNING * (depth + 1)
        if GameCalculations.is_board_full(board):
            # If the last move filled the board and no one won, it is not necessary to search any further
            return None, 0
        if depth == 0:
            # If we have reached depth 0, we calculate the score of the current board and return it
            return None, self.score_position(board, value, enemy_value)
        if maxi:
            # Maximizing score
            max_score = -math.inf
            max_column = 0
            for column in range(board.columns):
                line = board.get_line_first_empty_cell_in_column(column)
                if line is not None:
                    board_copy = copy(board)
                    board_copy.set_value(line, column, value)
                    # We copy the board and do the move on the copy as to not destroy our initial board
                    new_score = self.minimax(board_copy, depth - 1, value, enemy_value, alpha, beta, False,
                                             Cell(line, column, value))[1]

                    # We calculate the score that will be achieved if this move is done and both players play perfectly
                    if new_score > max_score:
                        # If the new score is greater than the maximum score, we change the maximum score and the column
                        max_score = new_score
                        max_column = column
                    alpha = max(alpha, max_score)
                    if alpha >= beta:
                        # Using alpha-beta pruning, if the current minimum achievable score for the maximizing player is
                        # greater than the current maximum achievable score for the minimizing player, we can stop
                        # looking in this move, since it will not be chosen
                        break
            return max_column, int(max_score)
        else:
            # Minimizing score
            min_score = math.inf
            min_column = 0
            for column in range(board.columns):
                line = board.get_line_first_empty_cell_in_column(column)
                if line is not None:
                    board_copy = copy(board)
                    board_copy.set_value(line, column, enemy_value)
                    # We copy the board and do the move on the copy as to not destroy our initial board
                    new_score = self.minimax(board_copy, depth - 1, value, enemy_value, alpha, beta, True,
                                             Cell(line, column, enemy_value))[1]
                    # We calculate the score that will be achieved if this move is done and both players play perfectly
                    if new_score < min_score:
                        min_score = new_score
                        min_column = column
                    beta = min(beta, min_score)
                    if alpha >= beta:
                        # Using alpha-beta pruning, if the current minimum achievable score for the maximizing player is
                        # greater than the current maximum achievable score for the minimizing player, we can stop
                        # looking in this move, since it will not be chosen
                        break
            return min_column, int(min_score)

    def score_position(self, board, value, enemy_value):
        """
        Calculates the score of the current board state
        :param board: The board on which the move is made, an object of type Board
        :param value: The value used to represent the pieces of the player for which the method does the move, the
        maximizing player
        :param enemy_value: The value used to represent the pieces of the opposing player, the minimizing player
        :return: The score of the board state, an integer
        """
        score = 0
        board_cells = board.get_board()
        board_cells = [[board_cells[line][column].value for column in range(board.columns)] for line in
                       range(board.lines)]

        for line in range(board.lines):
            for column in range(board.columns - 3):
                score += self.evaluate_space(board_cells[line][column:column + 4], value, enemy_value,
                                             board.empty_value)
        for column in range(board.columns):
            column_cells = [board_cells[line][column] for line in range(board.lines)]
            for line in range(board.lines - 3):
                score += self.evaluate_space(column_cells[line:line + 4], value, enemy_value, board.empty_value)
        for line in range(board.lines - 3):
            for column in range(board.columns - 3):
                score += self.evaluate_space([board_cells[line + counter][column + counter] for counter in range(3)],
                                             value, enemy_value, board.empty_value)
                score += self.evaluate_space([board_cells[line + 3 - counter][column + counter]
                                              for counter in range(3)], value, enemy_value, board.empty_value)
        return score

    def evaluate_space(self, space, value, enemy_value, empty_value):
        """
        Evaluates the score of a space on the board
        :param space: The space for which the score is evaluated, a list of 4 integers
        :param value: The value used to represent the pieces of the player for which the method does the move, the
        maximizing player
        :param enemy_value: The value used to represent the pieces of the opposing player, the minimizing player
        :param empty_value: The value used to represent an empty cell on the board
        :return: The score of the space, an integer
        """
        value_count = space.count(value)
        empty_value_count = space.count(empty_value)
        enemy_value_count = space.count(enemy_value)
        if value_count == 4:
            return self.FOUR_IN_A_ROW_SCORE
        if value_count == 3 and empty_value_count == 1:
            return self.THREE_IN_A_ROW_SCORE
        if value_count == 2 and empty_value_count == 2:
            return self.TWO_IN_A_ROW_SCORE
        if value_count == 1 and empty_value_count == 3:
            return self.ONE_IN_A_ROW_SCORE
        if enemy_value_count == 4:
            return -self.FOUR_IN_A_ROW_SCORE
        if enemy_value_count == 3 and empty_value_count == 1:
            return -self.THREE_IN_A_ROW_SCORE
        if enemy_value_count == 2 and empty_value_count == 2:
            return -self.TWO_IN_A_ROW_SCORE
        if enemy_value_count == 1 and empty_value_count == 3:
            return -self.ONE_IN_A_ROW_SCORE
        return 0
