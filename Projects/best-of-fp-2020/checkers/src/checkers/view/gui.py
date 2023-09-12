import pygame

from checkers.tools.constants import BLACK, LAVA, ROWS, COLS, ROCK, SQUARE_SIZE, CROWN, YELLOW_PIC, PURPLE_PIC, PURPLE, \
    GREEN, WIDTH, HEIGHT, YELLOW


class GUI:
    PADDING = 15
    OUTLINE = 2
    def __init__(self, window, game):
        self._window = window
        self._game = game

    def get_row_col_from_mouse(self, pos):
        """
        takes the position of the mouse, and based on the square size, calculates the actual square we are in
        Example: if y-position is 750px, and our square is 100px height, we're in the 7'th row
        :param pos:
        :return:
        """
        x, y = pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        return row, col

    @staticmethod
    def piece_calculate_position(piece):
        """
        calculates x and y coordinates, and places the piece in the middle of the square
        :return:
        """
        piece.x = SQUARE_SIZE * piece.col + SQUARE_SIZE // 2
        piece.y = SQUARE_SIZE * piece.row + SQUARE_SIZE // 2

    def update(self):
        self.draw_board(self._window)
        self.draw_valid_moves(self._game.valid_moves)
        pygame.display.update()

    def draw_board(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self._game.board.get_piece(row, col)
                if piece != 0:
                    self.draw_piece(window, piece)

    def draw_squares(self, window):
        window.fill(BLACK)
        window.blit(LAVA, window.get_rect())
        # for row in range(ROWS):
        #     for col in range(row % 2, ROWS, 2):
        #         pygame.draw.rect(window, PURPLE,)
        #         window.blit(WATER, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 1:
                    window.blit(ROCK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_piece(self, window, piece):
        radius = SQUARE_SIZE // 2 - GUI.PADDING
        # pygame.draw.circle(window, WHITE, (piece.x, piece.y), radius + GUI.OUTLINE)

        if piece.color == PURPLE:
            player1_rect = (piece.x - PURPLE_PIC.get_width() // 2, piece.y - PURPLE_PIC.get_height() // 2)
            window.blit(PURPLE_PIC, player1_rect)
        else:
            player1_rect = (piece.x - YELLOW_PIC.get_width() // 2, piece.y - YELLOW_PIC.get_height() // 2)
            window.blit(YELLOW_PIC, player1_rect)

        if piece.king == True:
            image_rect = (piece.x - CROWN.get_width() // 2, piece.y - CROWN.get_height() // 2)
            window.blit(CROWN, image_rect)

    def draw_valid_moves(self, moves):
        for move in moves:
            try:
                row, col = move
                pygame.draw.circle(self._window, GREEN,
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 20)
            except ValueError as ve:
                print(str(ve))

    # def variable_name_str(self, obj, namespace):
    #     return [name for name in namespace if namespace[name] is obj]

    def winner_name(self, color):
        if color == YELLOW:
            return "FIRE"
        else:
            return "ICE"

    def end_game(self, color):
        self._window.fill(color)
        pygame.display.set_caption("End of game!")
        pygame.font.init()
        font = pygame.font.Font(None, 72)
        text = font.render('Winner is ' + self.winner_name(color) + ' player' , True, BLACK, color)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        self._window.blit(text, textRect)
        pygame.display.update()
