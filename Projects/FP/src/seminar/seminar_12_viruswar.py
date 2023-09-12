"""
Virus War Game - http://www.papg.com/show?5SB0
"""


class Board:
    def __init__(self, size):
        self._size = size
        """
        0 - empty square
        1 - live X
        2 - live O
        3 - dead X
        4 - dead O
        """
        self._data = [[0 for x in range(size)] for y in range(size)]

    def _is_connected(self, x, y, symbol):
        # TODO Better way of representing data
        enemy_dead_virus = None
        if symbol == 1:
            enemy_dead_virus = 4
        else:
            enemy_dead_virus = 3

        queue = [(x, y)]
        # List of coordinates that we've already checked
        visited = []

        while len(queue) > 0:
            pos = queue.pop(0)
            visited.append(pos)

            x = pos[0]
            y = pos[1]
            # TODO Check if this is needed
            if self._data[x][y] == symbol:
                return True
            # if self._data[x][y] == enemy_dead_virus:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # don't put the same cell back in the queue
                    if i == 0 and j == 0:
                        continue
                    # don't step outside of the matrix
                    if x + i < 0 or x + i >= self._size or y + j < 0 or y + j >= self._size:
                        continue
                    if self._data[x + i][y + j] == symbol:
                        return True
                    # continue over dead virus
                    if self._data[x + i][y + j] == enemy_dead_virus and (x + i, y + j) not in visited:
                        queue.append((x + i, y + j))
        return False

    def get_valid_moves(self, symbol):
        """
        Valid moves for player symbol
        """
        if symbol not in [1, 2]:
            raise Exception('Bad symbol')

        moves = []

        for row in range(self._size):
            for col in range(self._size):
                cell = self._data[row][col]
                # Cannot place on top of your own live virus
                if cell == symbol:
                    continue
                # Cannot place on top of dead virus
                if cell in [3, 4]:
                    continue
                # If over an empty square or an enemy live virus
                if self._is_connected(row, col, symbol):
                    moves.append((row, col))

        return moves

    def move(self, x, y, symbol):
        """
        symbol - one of 'X', 'O'
        """
        # Move outside board
        if x < 0 or y < 0 or x >= self._size or y >= self._size:
            raise Exception("Move outside board!")
        # Move on top of your own symbol
        if (x, y) in self.get_valid_moves(symbol):
            self._data[x][y] = symbol
        else:
            raise Exception("Not a valid move")

    def __str__(self):
        # Board as string
        pass


b = Board(6)
# b.move(0, 0, 2)
b._data[1][1] = 3
b._data[2][2] = 3

print(b.get_valid_moves(1))
