"""
    The user interface for Tic Tac Toe
"""
from src.lecture.lecture_04.domain.board import init_board, to_str
from src.lecture.lecture_04.game.functions import is_game_won, is_game_draw, move_human, move_computer


def read_coord():
    row = int(input("X="))
    col = int(input("Y="))
    return row, col


def start():
    """
    Start the game
    """
    board = init_board()
    is_human_turn = True

    while not is_game_won(board) and not is_game_draw(board):
        print(to_str(board))
        if is_human_turn:
            try:
                human_move = read_coord()
                # *human_move unpacks the tuple into 2 params
                # move_human(board, human_move[0], human_move[1])
                move_human(board, *human_move)
            except ValueError as verr:
                print(str(verr))
                continue
            # except TypeError as verr:
            #     print(str(verr))
        else:
            move_computer(board)

        is_human_turn = not is_human_turn

    # TODO Give a message regarding victory / draw


start()
