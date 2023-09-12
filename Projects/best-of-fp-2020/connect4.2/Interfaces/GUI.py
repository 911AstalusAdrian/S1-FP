import math

import pygame

from Domain.Board import Board, BoardException
from Domain.Player import Player
from Game.Connect4 import Connect4


class Background(pygame.sprite.Sprite):
    """ Background class """

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Image(pygame.sprite.Sprite):
    """ Image class """

    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = location


class Button(Image):
    """ Button class """

    def __init__(self, image_file, location):
        super().__init__(image_file, location)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = location

    def is_selected(self, mouse):
        if self.rect.left <= mouse[0] <= self.rect.left + self.rect.size[0] \
                and self.rect.top <= mouse[1] <= self.rect.top + self.rect.size[1]:
            return True
        return False


class TextButton(pygame.sprite.Sprite):
    """ Text class """

    def __init__(self, text, location):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.rect = self.text.get_rect()
        self.rect.left, self.rect.centery = location

    def is_selected(self, mouse):
        if self.rect.left <= mouse[0] <= self.rect.left + self.rect.size[0] \
                and self.rect.top <= mouse[1] <= self.rect.top + self.rect.size[1]:
            return True
        return False


class Connect4GUI:
    def __init__(self, strategy):
        pygame.display.set_caption("Connect 4")
        pygame.init()  # initialize pygame
        pygame.font.init()  # initialize pygame's font module

        # initial settings of the game:
        self._height = 6  # the board height
        self._width = 7  # the board width
        self._winning_pieces = 4  # the pieces required to win
        self._player1 = Player('h', 1, 'red_button.png')
        self._player2 = Player('c', 2, 'yellow_button.png')
        self._strategy = strategy  # the ai strategy used
        self._AI_intelligence = 4  # the ai intelligence
        self._background = Background('Assets/background.png', [0, 0])  # the background image
        self._resolution = [1024, 768]  # the screen resolution
        self._screen = pygame.display.set_mode(self._resolution)  # the screen
        self._font = pygame.font.SysFont("berlinsansfb", 48)

    def run_menu(self):
        """ Runs the main menu """
        running = True
        title = Image('Assets/logo.png', [self._resolution[0] / 2, self._resolution[1] / 6])
        buttons = []  # button list

        play_button = Button('Assets/play_button.png', [self._resolution[0] / 2, self._resolution[1] / 1.9])
        settings_button = Button('Assets/settings_button.png', [self._resolution[0] / 2, self._resolution[1] / 1.1])

        buttons.append(play_button)
        buttons.append(settings_button)

        while running:
            mouse = pygame.mouse.get_pos()
            self._screen.fill([255, 255, 255])
            self._screen.blit(self._background.image, self._background.rect)
            self._screen.blit(title.image, title.rect)
            self._screen.blit(play_button.image, play_button.rect)
            self._screen.blit(settings_button.image, settings_button.rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.is_selected(mouse):
                        self.play_game()

                    if settings_button.is_selected(mouse):
                        self.run_settings()

            pygame.display.flip()

        pygame.quit()

    def run_settings(self):
        """ Runs the settings menu """
        done = False
        title = Image("Assets/settings_button.png", [self._resolution[0] / 2, self._resolution[1] / 10])

        # make the player switches
        player1_text = "Player 1: " + ('human' if self._player1.type == 'h' else 'computer')
        player1_color = [50, 50, 200]
        player1_switch = TextButton(self._font.render(player1_text, True, player1_color), [200, 300])

        player2_text = "Player 2: " + ('human' if self._player2.type == 'h' else 'computer')
        player2_color = [50, 50, 200]
        player2_switch = TextButton(self._font.render(player2_text, True, player2_color), [200, 400])

        # make the ai intelligence switch
        ai_intel_text = "AI intelligence: " + str(self._AI_intelligence)
        ai_intel_color = [50, 50, 200]
        ai_intel_switch = TextButton(self._font.render(ai_intel_text, True, ai_intel_color), [200, 500])

        # make the save button
        save_button = TextButton(self._font.render('Save', True, [0, 120, 0]), [200, 600])

        while not done:
            mouse = pygame.mouse.get_pos()

            self._screen.fill([255, 255, 255])
            self._screen.blit(self._background.image, self._background.rect)
            self._screen.blit(title.image, title.rect)
            self._screen.blit(player1_switch.text, player1_switch.rect)
            self._screen.blit(player2_switch.text, player2_switch.rect)
            self._screen.blit(ai_intel_switch.text, ai_intel_switch.rect)
            self._screen.blit(save_button.text, save_button.rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player1_switch.is_selected(mouse):
                        self._player1.type = 'h' if self._player1.type == 'c' else 'c'
                        player1_text = "Player 1: " + ('human' if self._player1.type == 'h' else 'computer')
                        player1_switch = TextButton(self._font.render(player1_text, True, player1_color), [200, 300])
                    elif player2_switch.is_selected(mouse):
                        self._player2.type = 'h' if self._player2.type == 'c' else 'c'
                        player2_text = "Player 2: " + ('human' if self._player2.type == 'h' else 'computer')
                        player2_switch = TextButton(self._font.render(player2_text, True, player2_color), [200, 400])
                    elif ai_intel_switch.is_selected(mouse):
                        self._AI_intelligence = 1 if self._AI_intelligence == 7 else self._AI_intelligence + 1
                        ai_intel_text = "AI intelligence: " + str(self._AI_intelligence)
                        ai_intel_switch = TextButton(self._font.render(ai_intel_text, True, ai_intel_color), [200, 500])
                    elif save_button.is_selected(mouse):
                        done = True

            pygame.display.flip()

    def play_game(self):
        clock = pygame.time.Clock()
        game_running = True
        game_over = False
        board_label = Image('Assets/board.png', [400, 350])
        board_shadow = Image('Assets/board_shadow.png', [400, 357])

        yellow_badge = Image('Assets/yellow_badge.png', [900, 400])
        red_badge = Image('Assets/red_badge.png', [900, 150])
        player1_icon = Image('Assets/' + ('human' if self._player1.type == 'h' else 'computer') + '_icon.png',
                             [900, 150])
        player2_icon = Image('Assets/' + ('human' if self._player2.type == 'h' else 'computer') + '_icon.png',
                                     [900, 400])

        board = Board(self._height, self._width, self._winning_pieces)
        strategy = self._strategy(board, self._AI_intelligence)
        game = Connect4(board, strategy, self._player1, self._player2)

        status_text = "Player 1's turn"
        status_label = TextButton(self._font.render(status_text, True, [255, 0, 0]), [50, 720])

        # initialize a matrix to keep track of already generated pieces
        piece_placed = []

        for row in range(board.height):
            matrix_row = []
            for col in range(board.width):
                matrix_row.append(0)
            piece_placed.append(matrix_row)

        # list in which we will keep the piece labels for blitting
        piece_labels = []

        while game_running:
            clock.tick(10)
            self._screen.fill([255, 255, 255])
            self._screen.blit(self._background.image, self._background.rect)
            self._screen.blit(board_shadow.image, board_shadow.rect)
            self._screen.blit(status_label.text, status_label.rect)
            self._screen.blit(yellow_badge.image, yellow_badge.rect)
            self._screen.blit(red_badge.image, red_badge.rect)
            self._screen.blit(player1_icon.image, player1_icon.rect)
            self._screen.blit(player2_icon.image, player2_icon.rect)

            for piece in piece_labels:
                self._screen.blit(piece.image, piece.rect)

            self._screen.blit(board_label.image, board_label.rect)

            current_player = game.get_current_player()

            mouse = pygame.mouse.get_pos()

            if current_player.type == 'h' and not game_over:  # if it's a humans turn, put an indicator for the column
                if 16 <= mouse[1] <= 684 and 50 <= mouse[0] <= 750:
                    pos = math.floor((mouse[0] - 50) / 100 + 1) * 100
                    indicator = Image('Assets/indicator.png', [pos, 700])
                    self._screen.blit(indicator.image, indicator.rect)

            pygame.display.flip()

            if board.won():
                if current_player.id == 1:
                    status_text = "Player 2 won the game."
                    status_label = TextButton(self._font.render(status_text, True, [255, 236, 21]), [50, 720])
                else:
                    status_text = "Player 1 won the game."
                    status_label = TextButton(self._font.render(status_text, True, [255, 0, 0]), [50, 720])
                game_over = True
            elif board.is_full():
                status_text = "Stalemate."
                status_label = TextButton(self._font.render(status_text, True, [40, 100, 255]), [50, 720])
                game_over = True

            if current_player.type == 'c' and not game_over:
                game.next_computer_move()
                if current_player.id == 1:
                    status_text = "Player 2's turn."
                    status_label = TextButton(self._font.render(status_text, True, [255, 236, 21]),
                                              [50, 720])
                else:
                    status_text = "Player 1's turn."
                    status_label = TextButton(self._font.render(status_text, True, [255, 0, 0]),
                                              [50, 720])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False  # return to the main menu when the window x button is pressed

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if current_player.type == 'h' and not game_over:
                        if event.button == 1:  # check if the left mouse button has been pressed
                            if 16 <= mouse[1] <= 684 and 50 <= mouse[0] <= 750:
                                move = (mouse[0] - 50) / 100
                                try:
                                    game.next_human_move(math.floor(move))
                                    if current_player.id == 1:
                                        status_text = "Player 2's turn."
                                        status_label = TextButton(self._font.render(status_text, True, [255, 236, 21]),
                                                                  [50, 720])
                                    else:
                                        status_text = "Player 1's turn."
                                        status_label = TextButton(self._font.render(status_text, True, [255, 0, 0]),
                                                                  [50, 720])
                                except BoardException:
                                    print("oopsie :)")

            # update the table
            for row in range(board.height):
                for col in range(board.width):
                    if board[row][col].is_filled() and piece_placed[row][col] == 0:  # check if the piece has not been
                        # generated yet
                        piece = Image('Assets/' + current_player.piece, [100 + col * 100, 100 + row * 100])
                        piece_labels.append(piece)
                        piece_placed[row][col] = 1
