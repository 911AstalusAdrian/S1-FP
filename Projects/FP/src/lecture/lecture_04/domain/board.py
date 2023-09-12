"""
Functions for managing the game board
    - exceptions!
    - unit tests!
"""


def to_str(board):
    res = ''
    for row in range(3):
        for col in range(3):
            char = get_slot(board, row, col)
            res += '_' if char is None else char
            # if  char is None:
            #     res += '_'
            # else:
            #     res += char
        res += '\n'
    return res


def init_board():
    """
    Init an empty board
    return the empty board
    """
    #     Valid values for a square
    #         None -> empty square
    #            O -> 'O'
    #            X -> 'X'
    # TODO Check and see what works here
    # board = [[None * 3] for i in range(3)]
    board = [[None for j in range(3)] for i in range(3)]
    return board


def set_slot(board, x, y, char):
    board[x][y] = char


def get_slot(board, x, y):
    # 012
    # 345
    # 678
    return board[x][y]


def move(board, x, y, char):
    """
    Make a move!
    board - The board
    x,y - int coordinates in [0,2]
    char - one of 'O', or 'X'
    Raise ValueError if:
        - try to place on an occupied slot
        - try to place outside the bounds
        - try to place an invalid char
    """
    # if not (0 <= x <= 2) or ...
    if not (x in [0, 1, 2]) or not (y in [0, 1, 2]):
        raise ValueError('Move outside the board')
    if not (char.upper() in ['X', 'O']):
        raise ValueError('Invalid character')
    # Trying to place on a taken slot
    if not get_slot(board, x, y) is None:
        raise ValueError('Slot already taken')
    # Make the move
    set_slot(board, x, y, char)


def is_board_full(board):
    """
    Check if board is full
    return True if board is full, False otherwise
    """
    for row in range(3):
        for col in range(3):
            if get_slot(board, row, col) is None:
                # return as soon as we know
                return False
    return True


def test_move():
    # TODO Add more asserts
    b = init_board()

    try:
        move(b, 2,3,'X')
        assert False
    except ValueError:
        assert True

    for i in range(3):
        for j in range(3):
            move(b, i, j, 'X')
    assert is_board_full(b)

    try:
        move(b, 1, 1, 'O')
        assert False
    except ValueError:
        assert True


def test_init_board():
    b = init_board()
    assert type(b) == type([])
    # assert len(b) == 3
    for i in [0,1,2]:
        for j in [0, 1, 2]:
            assert get_slot(b, i, j) is None


def test_is_board_full():
    # TODO Complete test
    b = init_board()
    assert is_board_full(b) == False


test_init_board()
test_is_board_full()
test_move()





