import math
from random import randint


class MinimaxStrategy:
    def __init__(self, board, search_depth):
        self._board = board  # the game board
        self._computer = None  # the maximizing player
        self._opponent = None  # the minimizing player
        self._search_depth = search_depth  # the search max_depth of the algorithm

    def evaluate(self):
        """
        Check for patterns of 4 cells that contain only one piece type such as: _xxx, _o_o, _x_x, _oo_, and score them.
        :return: score of the board state
        """
        score = 0
        # check for patterns on the rows
        for row in range(self._board.height):
            for col in range(self._board.width - self._board.pieces_to_win + 1):
                empty_pieces = 0  # no. of empty pieces in current pattern
                pieces = 0  # no. of pieces in current pattern
                pattern_id = 0  # id of the player the current pattern belongs to
                for i in range(self._board.pieces_to_win):
                    if self._board.is_cell_empty(row, col + i):
                        empty_pieces += 1
                        if empty_pieces > 2:
                            break  # if we have more than 2 empty pieces on current pattern, skip it
                    else:
                        if pieces == 0:  # if this is the first piece of the pattern, it decides the pattern's owner
                            pattern_id = self._board[row][col + i].value
                            pieces += 1
                        else:  # if it is not the first piece, check if it fits the pattern
                            if not pattern_id == self._board[row][col + i].value:
                                break  # if the current pattern has mixed pieces, skip it
                            pieces += 1
                if pieces + empty_pieces == 4:  # if we found a pattern
                    if pattern_id == self._computer.id:
                        score += pieces * 10
                    else:
                        score -= pieces * 10

        # check for patterns on the columns
        for col in range(self._board.width):
            for row in range(self._board.height - self._board.pieces_to_win + 1):
                empty_pieces = 0
                pieces = 0
                pattern_id = 0
                for i in range(self._board.pieces_to_win):
                    if self._board.is_cell_empty(row + i, col):
                        empty_pieces += 1
                        if empty_pieces > 2:
                            break
                    else:
                        if pieces == 0:
                            pattern_id = self._board[row + i][col].value
                            pieces += 1
                        else:
                            if not pattern_id == self._board[row + i][col].value:
                                break
                            pieces += 1
                if pieces + empty_pieces == 4:
                    if pattern_id == self._computer.id:
                        score += pieces * 10
                    else:
                        score -= pieces * 10

        # check for patterns on the main diagonals
        for row in range(self._board.height - self._board.pieces_to_win + 1):
            for col in range(self._board.width - self._board.pieces_to_win + 1):
                i = 0
                while row + i < self._board.height - self._board.pieces_to_win and col + i < self._board.width - \
                        self._board.pieces_to_win:
                    empty_pieces = 0
                    pieces = 0
                    pattern_id = 0
                    for j in range(self._board.pieces_to_win):
                        if self._board.is_cell_empty(row + i + j, col + i + j):
                            empty_pieces += 1
                            if empty_pieces > 2:
                                break
                        else:
                            if pieces == 0:
                                pattern_id = self._board[row + i + j][col + i + j].value
                                pieces += 1
                            else:
                                if not pattern_id == self._board[row + i + j][col + i + j].value:
                                    break
                                pieces += 1
                        if pieces + empty_pieces == 4:
                            if pattern_id == self._computer.id:
                                score += pieces * 10
                            else:
                                score -= pieces * 10
                    i += 1

        # check for patterns on the secondary diagonals
        for row in range(self._board.pieces_to_win - 1, self._board.height):
            for col in range(self._board.width - self._board.pieces_to_win + 1):
                i = 0
                while row - i > 0 + self._board.pieces_to_win and col + i < self._board.width - \
                        self._board.pieces_to_win:
                    empty_pieces = 0
                    pieces = 0
                    pattern_id = 0
                    for j in range(self._board.pieces_to_win):
                        if self._board.is_cell_empty(row - i - j, col + i + j):
                            empty_pieces += 1
                            if empty_pieces > 2:
                                break
                        else:
                            if pieces == 0:
                                pattern_id = self._board[row - i - j][col + i + j].value
                                pieces += 1
                            else:
                                if not pattern_id == self._board[row - i - j][col + i + j].value:
                                    break
                                pieces += 1
                        if pieces + empty_pieces == 4:
                            if pattern_id == self._computer.id:
                                score += pieces * 10
                            else:
                                score -= pieces * 10
                    i += 1

        return score

    def minimax(self, alpha, beta, opponent_turn, max_depth):
        """
        Minimax algorithm that assigns a score to a potential move, with alpha-beta tree pruning.
        :param alpha: guaranteed minimum score for the computer player
        :param beta: guaranteed maximum score for the opposing player
        :param opponent_turn: bool representing whether or not it's the opponent's turn
        :param max_depth: the maximum search depth
        :return: the score for the terminal board state
        """
        if self._board.won():  # if the game state indicates a win
            if opponent_turn:  # if the opponent lost
                return 1000000 + max_depth  # add the current max_depth to prioritize faster winning moves
            else:  # if the computer lost
                return -1000000 - max_depth  # subtract the current max_depth to prioritize farther losing moves

        if self._board.is_full():  # if the board is filled or we reached the search max_depth
            return 0

        if max_depth == 0:
            return self.evaluate()

        if opponent_turn:  # if its the opponent's turn, we minimize the score
            best = math.inf
            for col in range(self._board.width):
                if self._board[0][col].is_empty():  # if the column's not filled, we consider it as the next move
                    self._board.place_piece(col, self._opponent.id)
                    move = self.minimax(alpha, beta, not opponent_turn, max_depth - 1)
                    best = min(best, move)
                    self._board.remove_piece(col)
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
            return best
        else:
            best = -math.inf
            for col in range(self._board.width):
                if self._board[0][col].is_empty():
                    self._board.place_piece(col, self._computer.id)
                    move = self.minimax(alpha, beta, not opponent_turn, max_depth - 1)
                    best = max(move, best)
                    self._board.remove_piece(col)
                    alpha = max(alpha, best)
                    if alpha >= beta:
                        break
            return best

    def next_move(self, computer, opponent):
        """
        Return the next optimal move for the computer
        :param computer: the computer player instance
        :param opponent: the opponent player instance
        :return: an integer representing the column of the move
        """
        scores = []  # list containing the scores for each available move
        self._computer = computer
        self._opponent = opponent

        for col in range(self._board.width):
            if self._board[0][col].is_empty():  # check if the column is not full
                self._board.place_piece(col, self._computer.id)
                score = self.minimax(-math.inf, math.inf, True, self._search_depth)
                self._board.remove_piece(col)
                scores.append((score, col))  # append the pair of the score and its column to the scores list

        # randomize the choice if we have multiple maximum scores with the same value:
        scores.sort(key=lambda x: x[0])  # sort the scores
        max_score = scores[len(scores) - 1]  # get the max score
        scores = list(filter(lambda x: x[0] == max_score[0], scores))  # filter so we only have the max scores

        return scores[randint(0, len(scores) - 1)][1]
