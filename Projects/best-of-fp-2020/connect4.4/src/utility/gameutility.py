class GameCalculations:
    WINNER_COUNT = 4

    @staticmethod
    def is_winner(board, move):
        """
        Checks if a move has won the game for the player that did it
        :param board: The board on which the game is played, an object of type Board
        :param move: The cell affected by the move, an object of type Cell
        :return: True if the move won the game for the player that did it, otherwise False
        """
        if board.count_connected_pieces_to_cell_on_column(move) >= GameCalculations.WINNER_COUNT or \
           board.count_connected_pieces_to_cell_on_line(move) >= GameCalculations.WINNER_COUNT or \
           board.count_connected_pieces_to_cell_on_principal_diagonal(move) >= GameCalculations.WINNER_COUNT or \
           board.count_connected_pieces_to_cell_on_secondary_diagonal(move) >= GameCalculations.WINNER_COUNT:
            return True
        return False

    @staticmethod
    def is_board_full(board):
        """
        Checks if the board is full of pieces
        :param board: The board that will be checked, an object of type Board
        :return: True if the board is full, otherwise False
        """
        for column in range(board.columns):
            if board.get_line_first_empty_cell_in_column(column) is not None:
                return False
        return True
