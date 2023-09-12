from Domain.Board import Board


class TestFileParser:
    def __init__(self, file):
        self._file = file

    def get_boards_from_file(self):
        """
        Parses the files and extracts all the game boards and the arguments, in which 'x' - represents player 1 piece,
        'o' - represents player 2 piece and '_' - represents empty piece

        :return: yields all the tables in the file with their arguments
        """
        line = self._file.readline()

        while line != '':
            board = Board(6, 7, 4)

            for row in range(board.height):
                for col in range(board.width):
                    if line[col] == 'x':
                        board[row][col].value = 1
                    elif line[col] == 'o':
                        board[row][col].value = 2
                line = self._file.readline()
            yield line, board
            line = self._file.readline()
            line = self._file.readline()
