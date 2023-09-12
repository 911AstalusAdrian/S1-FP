import random


class RandomMoveStrategy:
    @staticmethod
    def get_next_move(board):
        """
        Finds a random valid square to make a move on the board
        :param board: the given board
        :return: a tuple with the indices of the move
        """
        available_positions = board.get_available_squares()

        rand_pos = random.randrange(0, len(available_positions))

        return available_positions[rand_pos]


class AIStrategy:
    def __init__(self, mode="hard"):
        self._INF = float("inf")
        self._depth = None
        self._max_comparisons = None
        if mode == "extreme":
            self._depth = 1
            self._max_comparisons = self._INF
        elif mode == "hard":
            self._depth = 0
            self._max_comparisons = self._INF
        elif mode == "easy":
            self._depth = 0
            self._max_comparisons = 20

    @staticmethod
    def get_shape_score(consecutive, open_ends, current_turn):
        """
        Computes the score of the given shape
        :param consecutive: number of consecutive elements
        :param open_ends: number of open ends of the shape
        :param current_turn: a boolean telling us whether it is the player's turn now
        :return: the score associated to the shape
        """
        if consecutive == 5:
            return 200000000

        if open_ends == 0:
            return 0

        if consecutive == 4:
            if open_ends == 1:
                if current_turn is True:
                    return 100000000
                return 50
            elif open_ends == 2:
                if current_turn is True:
                    return 100000000
                return 500000

        if consecutive == 3:
            if open_ends == 1:
                if current_turn is True:
                    return 7
                return 5
            elif open_ends == 2:
                if current_turn is True:
                    return 10000
                return 50

        if consecutive == 2:
            if open_ends == 1:
                return 2
            else:
                return 5

        if open_ends == 1:
            return 1
        return 0.5

    def evaluate_lines(self, board, symbol, current_turn):
        """
        Checks the board for lines of consecutive symbols
        :param board: the board
        :param symbol: the given symbol
        :param current_turn: a boolean telling us whether it is the player's turn now
        :return: a score computed in relation to the shapes found
        """
        n = board.row_size
        consecutive = [0, 0]
        open_ends = [0, 0]
        score = 0

        for i in range(n):
            for j in range(n):
                # Check horizontally
                if board.is_symbol(i, j, symbol) is True:
                    consecutive[0] += 1
                elif board.is_square_empty(i, j) is True and consecutive[0] > 0:
                    open_ends[0] += 1
                    score += self.get_shape_score(consecutive[0], open_ends[0], current_turn)
                    consecutive[0] = 0
                    open_ends[0] = 1
                elif board.is_square_empty(i, j) is True:
                    open_ends[0] = 1
                elif consecutive[0] > 0:
                    score += self.get_shape_score(consecutive[0], open_ends[0], current_turn)
                    consecutive[0] = 0
                    open_ends[0] = 0
                else:
                    open_ends[0] = 0

                # Check vertically
                if board.is_symbol(j, i, symbol) is True:
                    consecutive[1] += 1
                elif board.is_square_empty(j, i) is True and consecutive[1] > 0:
                    open_ends[1] += 1
                    score += self.get_shape_score(consecutive[1], open_ends[1], current_turn)
                    consecutive[1] = 0
                    open_ends[1] = 1
                elif board.is_square_empty(j, i) is True:
                    open_ends[1] = 1
                elif consecutive[1] > 0:
                    score += self.get_shape_score(consecutive[1], open_ends[1], current_turn)
                    consecutive[1] = 0
                    open_ends[1] = 0
                else:
                    open_ends[1] = 0

            # Check horizontally
            if consecutive[0] > 0:
                score += self.get_shape_score(consecutive[0], open_ends[0], current_turn)

            # Check vertically
            if consecutive[1] > 0:
                score += self.get_shape_score(consecutive[1], open_ends[1], current_turn)

            consecutive = [0, 0]
            open_ends = [0, 0]

        return score

    def evaluate_diagonal_lines(self, board, symbol, current_turn):
        """
        Checks the board for diagonal lines of consecutive symbols
        :param board: the board
        :param symbol: the given symbol
        :param current_turn: a boolean telling us whether it is the player's turn now
        :return: a score computed in relation to the shapes found
        """
        n = board.row_size
        consecutive = [0, 0]
        open_ends = [0, 0]
        score = 0

        for d in range(2 * n - 1):
            size = n - abs(n - 1 - d)
            start = max(0, d - n + 1)
            diff = d - n + 1

            for i in range(start, start + size):
                j = [i - diff, d - i]

                # Check diagonally parallel to the main one
                if board.is_symbol(i, j[0], symbol) is True:
                    consecutive[0] += 1
                elif board.is_square_empty(i, j[0]) is True and consecutive[0] > 0:
                    open_ends[0] += 1
                    score += self.get_shape_score(consecutive[0], open_ends[0], current_turn)
                    consecutive[0] = 0
                    open_ends[0] = 1
                elif board.is_square_empty(i, j[0]) is True:
                    open_ends[0] = 1
                elif consecutive[0] > 0:
                    score += self.get_shape_score(consecutive[0], open_ends[0], current_turn)
                    consecutive[0] = 0
                    open_ends[0] = 0
                else:
                    open_ends[0] = 0

                # Check diagonally parallel to the secondary one
                if board.is_symbol(i, j[1], symbol) is True:
                    consecutive[1] += 1
                elif board.is_square_empty(i, j[1]) is True and consecutive[1] > 0:
                    open_ends[1] += 1
                    score += self.get_shape_score(consecutive[1], open_ends[1], current_turn)
                    consecutive[1] = 0
                    open_ends[1] = 1
                elif board.is_square_empty(i, j[1]) is True:
                    open_ends[1] = 1
                elif consecutive[1] > 0:
                    score += self.get_shape_score(consecutive[1], open_ends[1], current_turn)
                    consecutive[1] = 0
                    open_ends[1] = 0
                else:
                    open_ends[1] = 0

            # Check diagonally parallel to the main one
            if consecutive[0] > 0:
                score += self.get_shape_score(consecutive[0], open_ends[0], current_turn)

            # Check diagonally parallel to the secondary one
            if consecutive[1] > 0:
                score += self.get_shape_score(consecutive[1], open_ends[1], current_turn)

            consecutive = [0, 0]
            open_ends = [0, 0]

        return score

    def evaluate_board(self, board, computer_symbol, human_symbol, computer_turn):
        """
        Checks the state of the board
        :param board: the given board
        :param computer_symbol: the symbol the computers (maximizer) uses
        :param human_symbol: the symbol the human (minimizer) uses
        :param computer_turn: a boolean value telling us whether it is the computer's (maximizer's) turn
        :return: a score corresponding to the current board
        """
        score = self.evaluate_lines(board, computer_symbol, computer_turn)
        score += self.evaluate_diagonal_lines(board, computer_symbol, computer_turn)
        score -= self.evaluate_lines(board, human_symbol, not computer_turn)
        score -= self.evaluate_diagonal_lines(board, human_symbol, not computer_turn)
        return score

    def minimax(self, board, is_first, max_turn, depth, alpha, beta):
        """
        The minimax algorithm for computing the best possible move
        :param board: the board the game is played on
        :param is_first: a boolean value telling us if the maximizer played first
        :param max_turn: a boolean value telling us if it is the maximizer's turn
        :param depth: the current depth
        :param alpha: the value of alpha used for alpha-beta pruning
        :param beta: the value of beta used for alpha-beta pruning
        :return: the best possible score
        """
        computer_symbol = 'O' if is_first is True else 'X'
        human_symbol = 'X' if is_first is True else 'O'

        if depth == 0:
            return self.evaluate_board(board, computer_symbol, human_symbol, max_turn)

        available = board.get_available_squares()
        best_value = self._INF

        if len(available) == 0:
            return 0

        if max_turn is True:
            best_value = -best_value

        count = 0
        random.shuffle(available)

        for i, j in available:
            if board.has_neighbours(i, j) is False:
                continue

            count += 1

            board.make_move(i, j, computer_symbol if max_turn is True else human_symbol)

            move_score = self.minimax(board, is_first, not max_turn, depth - 1, alpha, beta)

            if max_turn is True:
                best_value = max(best_value, move_score)
                alpha = max(alpha, best_value)
            else:
                best_value = min(best_value, move_score)
                beta = min(beta, best_value)

            board.delete_move(i, j)

            if beta <= alpha:
                break

            if count == self._max_comparisons:
                break

        return best_value

    def get_next_move(self, board, is_first):
        """
        Finds the best move for the AI
        :param board: the board on which the game is played
        :param is_first: a boolean which tells us if the computer moved first
        :return: a tuple containing indices of the best move
        """
        available = board.get_available_squares()
        best_value = -self._INF
        best_move = (-1, -1)
        computer_symbol = 'O' if is_first else 'X'
        count = 0
        random.shuffle(available)

        if len(available) == 0:
            return -1, -1

        for i, j in available:
            if board.has_neighbours(i, j) is False:
                continue

            count += 1

            board.make_move(i, j, computer_symbol)
            move_value = self.minimax(board, is_first, False, self._depth, -self._INF, self._INF)
            board.delete_move(i, j)

            if move_value > best_value:
                best_value = move_value
                best_move = (i, j)

            if count == self._max_comparisons:
                break

        if best_move[0] == -1 and best_move[1] == -1:
            return available[random.randrange(0, len(available))]

        return best_move
