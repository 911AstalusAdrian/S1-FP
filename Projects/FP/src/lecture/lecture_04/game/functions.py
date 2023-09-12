"""
Functions to manage the game
    - no UI
    - calls methods from board
"""

from src.lecture.lecture_04.domain.board import get_slot, move, init_board, is_board_full

'''
    This is called the Strategy Design Pattern
'''


def is_game_draw(board):
    return is_board_full(board) and not is_game_won(board)


def is_game_won(board):
    # TODO Implement this
    return False


def move_computer_smart(board):
    """
    ...
    """
    # TODO Make computer play smart moves
    pass


def move_computer_random(board):
    """
    ...
    """
    # TODO Make computer play random, but valid moves
    pass


# TODO Should check for full board
def move_computer_simple(board):
    """
    Make the computer's next move (O)
    """
    for row in range(3):
        for col in range(3):
            if get_slot(board, row, col) is None:
                # Computer always plays with O
                move(board, row, col, 'O')
                return
    raise ValueError('Cannot make move on a full board')


def move_computer(board):
    move_computer_simple(board)
    # move_computer_random(board)
    # move_computer_smart(board)

def move_human(board, row, col):
    """
    Make the human's move
    Raise ValueError if its an invalid move
    """
    move(board, row, col, 'X')


def test_move_computer():
    b = init_board()
    for i in range(3):
        for j in range(3):
            move_computer(b)
            assert get_slot(b, i, j) == 'O'

    assert is_board_full(b)


test_move_computer()

