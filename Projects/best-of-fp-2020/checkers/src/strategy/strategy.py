from copy import deepcopy
import pygame

from checkers.tools.constants import YELLOW, PURPLE


class Strategy:
    def __init__(self):
        pass

    @staticmethod
    def minimax(position, depth, max_player):
        """

        :param position: the current position we are in (a board object)
        :param depth: how far are we extending our tree
        :param max_player: boolean value - max_player = true => we maximize the score, max-player = false => we minimize it
        :param game: game object, passed to the algorithm to potentially draw stuff
        :return: the score (evaluation) of the board, and the board object
        """

        if depth == 0 or position.winner() is not None:
            return position.evaluate(), position

        #we maximize the score
        if max_player:
            max_score = float('-inf')
            all_moves = Strategy.get_all_moves(position, YELLOW) #we get all the moves for the current player (computer)
            best_move_board = None
            for move in all_moves:
                #then we evaluate all the moves of the player, and pick the one with the highest score
                score = Strategy.minimax(move, depth - 1, False)[0] #the score only
                max_score = max(max_score, score)
                if max_score == score:
                    best_move_board = move

            return max_score, best_move_board
        else:
            min_score = float('inf')
            all_moves = Strategy.get_all_moves(position, PURPLE)#we get all the moves for the current player (human)
            best_move_board = None
            for move in all_moves:
                #then we evaluate all the moves of the player, and pick the one with the minimum score
                score = Strategy.minimax(move, depth - 1, True)[0]  # the score only
                min_score = min(min_score, score)
                if min_score == score:
                    best_move_board = move

            return min_score, best_move_board

    @staticmethod
    def get_all_moves(board, color):
        moves = []
        all_pieces = board.get_all_pieces(color)
        for piece in all_pieces:
            valid_moves = board.get_valid_moves(piece)
            for move, skipped in valid_moves.items():
                temporary_board = deepcopy(board)
                temporary_piece = temporary_board.get_piece(piece.row, piece.col)
                new_board = Strategy.simulate_move(temporary_piece, move, temporary_board, skipped)
                moves.append(new_board)
        return moves

    @staticmethod
    def simulate_move(piece, move, board, skipped):
        board.move(piece, move[0], move[1])
        if skipped:
            board.remove(skipped)

        return board
