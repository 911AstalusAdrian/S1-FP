from random import randint, choice

from engines.ai import AI
from persistence.rules import Rules


class HardAI(AI):
    """
    Hard level AI

    Randomised ship placement

    Statistics based shooting:
        Try to fit all the ships on the board, thus creating a score for each cell (in how many ways can the ships
        placement contain that cell)
        Choose the cell with the highest score
        In case of equality the choice is random

        The cells to the N, W, S, E of a hit bun not sunk cell are greatly increased for hunting

        In the no touch mode (default) cells around a sunken ship are weighted as the hit/miss cells
        (no ship part can be found there)
    """
    def __init__(self, own_board, opponent_board):
        super().__init__(own_board, opponent_board)
        self._directions = {
            'w':    {'line': 0, 'column': -1},
            'nw':   {'line': -1, 'column': -1},
            'n':    {'line': -1, 'column': 0},
            'ne':   {'line': -1, 'column': 1},
            'e':    {'line': 0, 'column': 1},
            'se':   {'line': 1, 'column': 1},
            's':    {'line': 1, 'column': 0},
            'sw':   {'line': 1, 'column': -1}
        }
        self._ships = {
            'destroyer': 2,
            'cruiser': 3,
            'submarine': 3,
            'battleship': 4,
            'carrier': 5
        }
        self._score_board = self._compute_points()

    @property
    def score_board(self):
        """
        The score board but all the values are floats in the [0, 1] interval
        """
        normalised_score_board = self._score_board[:]
        maximum = 0
        for score in normalised_score_board:
            if score > maximum:
                maximum = score

        return [score/maximum for score in normalised_score_board]

    def _position_in_bounds(self, line, column):
        """ Return True if the position (line, column) is within the bounds of the ship """
        return 0 <= line < self._edge_size and 0 <= column < self._edge_size

    def _prepare_base_board(self):
        """
        Creates and returns a base board.
        The base board is a 0/1 board where:
            1 = a cell in which a ship part can be (not an already shot cell or not a cell around a sunken ship)
            0 = a cell in which a ship part cannot be
        """
        initial_board = self._opponent_board.values
        base_board = self._opponent_board.values

        for line in range(10):
            for column in range(10):
                cell = line * 10 + column
                value = initial_board[cell]

                if value == '+':
                    base_board[cell] = 0
                elif value == '-':
                    base_board[cell] = 0
                elif value == '*':
                    base_board[cell] = 0
                    if not Rules().can_touch:
                        self._make_0_border_of_cell(base_board, line, column)
                else:
                    base_board[cell] = 1 if base_board[cell] != 0 else 0

        return base_board

    def _make_0_border_of_cell(self, base_board, line, column):
        """
        0's the cells neighboring the sunken ship's cell
        """
        for direction in self._directions:
            next_line = line + self._directions[direction]['line']
            next_column = column + self._directions[direction]['column']
            if self._position_in_bounds(next_line, next_column):
                cell = next_line * self._edge_length + next_column
                base_board[cell] = 0

    def _compute_points(self):
        """
        Creates a score board where all the cells contain how many ship parts could be placed in that cell.
        If it is nearby a hit but not sunken ship, the score is greatly increased
        :return:
        """
        base_board = self._prepare_base_board()
        score_board = [0] * Rules().edge * Rules().edge

        self._hit_but_not_sunk_scores(score_board)

        for ship in self._ships:
            if self._opponent_board.ships_left[ship] > 0:
                self.__compute_points_for_ship(score_board, base_board, ship)

        return score_board

    def __compute_points_for_ship(self, score_board, base_board, ship):
        """
        Internal method for _compute_points
        """
        # Add the points for one ship type to the score board
        length = self._ships[ship]

        for line in range(self._edge_size):
            for column in range(self._edge_size):
                cell = line * self._edge_size + column
                if base_board[cell] == 0:
                    score_board[cell] = 0
                else:
                    # try to fit in both orientations
                    if self._does_it_fit(base_board, line, column, length, 'vertical'):
                        self._increase_score(score_board, line, column, length, 'vertical')
                    if self._does_it_fit(base_board, line, column, length, 'horizontal'):
                        self._increase_score(score_board, line, column, length, 'horizontal')

    def _does_it_fit(self, base_board, line, column, length, orientation):
        """
        Checks if the boat with the given 'length' would fit on the base board (not touch a 0 cell) starting from the
        line and column with the given orientation:
            if vertical it goes to south
            if horizontal it goes to east
        """
        direction = 's' if orientation == 'vertical' else 'e'

        for i in range(length):
            if not self._position_in_bounds(line, column):
                return False

            cell = line * self._edge_size + column
            if base_board[cell] == 0:
                return False

            line += self._directions[direction]['line']
            column += self._directions[direction]['column']

        return True

    def _increase_score(self, score_board, line, column, length, orientation):
        """
        Increase the score by 1 for all the cells starting with (line, column) for a given length in a given orientation
        """
        direction = 's' if orientation == 'vertical' else 'e'

        for i in range(length):
            cell = line * self._edge_size + column
            score_board[cell] += 1

            line += self._directions[direction]['line']
            column += self._directions[direction]['column']

    def __greatly_increase_scores(self, score_board, *coords):
        """ Increase the scores of the cells with the given coords by 'increase_value' """
        increase_value = 100

        for coord in coords:
            line = coord[0]
            column = coord[1]
            if not self._position_in_bounds(line, column):
                continue

            cell = line*self._edge_size + column
            score_board[cell] += increase_value

    def __where_is_continued(self, initial_board, line, column):
        """
        Returns the direction where the ship could continue (n, e, s, w)
        ex. If there is a ship part ('+') to the south the ship can still go to the north, thus it will return 'n'
            If there is a ship part both to the south and north it will return None (the ship is already continued in all possible sides)
        """
        possible_directions = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
        for direction in possible_directions:
            next_line = line + self._directions[direction]['line']
            next_column = column + self._directions[direction]['column']
            if not self._position_in_bounds(next_line, next_column):
                continue

            next_cell = next_line * self._edge_size + next_column
            if initial_board[next_cell] == '+':
                opposite_direction = possible_directions[direction]
                opposite_line = line + self._directions[opposite_direction]['line']
                opposite_column = column + self._directions[opposite_direction]['column']
                if not self._position_in_bounds(opposite_line, opposite_column):
                    continue
                opposite_cell = opposite_line * self._edge_size + opposite_column
                return opposite_direction if initial_board[opposite_cell] != '+' else None
        return '0'

    def _hit_but_not_sunk_scores(self, score_board):
        """ Adds to the initial board the scores for the ships that were hit and will be hunt """

        initial_board = self._opponent_board.values
        can_touch = Rules().can_touch

        for line in range(self._edge_size):
            for column in range(self._edge_size):
                cell = line * self._edge_size + column
                if initial_board[cell] == "+":
                    if can_touch:
                        self.__greatly_increase_scores(score_board, (line-1, column), (line, column+1), (line+1, column), (line, column-1))
                    else:
                        continuing_direction = self.__where_is_continued(initial_board, line, column)
                        if continuing_direction == '0':
                            self.__greatly_increase_scores(score_board, (line - 1, column), (line, column + 1),
                                                           (line + 1, column), (line, column - 1))
                        if continuing_direction in self._directions:
                            self.__greatly_increase_scores(score_board, (line + self._directions[continuing_direction]['line'],
                                                                         column + self._directions[continuing_direction]['column']))

    # def _maximal_cells(self, score_board):
    #     """
    #     Iterates through the score_board and returns a list of coordinates of the cells with the max score
    #     """
    #     max_score = 0
    #     max_cells = []
    #     edge_size = self._edge_size
    #
    #     for line in range(edge_size):
    #         for column in range(edge_size):
    #             cell = line * edge_size + column
    #             if score_board[cell] > max_score:
    #                 max_cells.clear()
    #                 max_cells.append((line, column))
    #                 max_score = score_board[cell]
    #             elif score_board[cell] == max_score:     # TODO test the accuracy (score_board[cell] == max_score)
    #                 max_cells.append((line, column))
    #     return max_cells

    def _maximal_cells(self, score_board):
        """
        Iterates through the score_board and returns a list of coordinates of the cells with the max score
        """
        max_score = 0
        max_cells = []
        edge_size = self._edge_size

        for line in range(edge_size):
            for column in range(edge_size):
                cell = line * edge_size + column
                if score_board[cell] > max_score:
                    max_cells.clear()
                    max_cells.append((line, column))
                    max_score = score_board[cell]
                elif max_score - score_board[cell] < 0.05:
                    max_cells.append((line, column))
        return max_cells

    def _compute_target_coords(self):
        self._score_board = self._compute_points()
        coords = choice(self._maximal_cells(self.score_board))

        line = coords[0] + 1
        column = coords[1] + 1

        return line, column
