
from checkers.board.board import Board
from checkers.game.game import Game, GameException
from checkers.tests import test_all
from checkers.view.gui import GUI
from checkers.view.ui import UI
from src.checkers.tools.constants import *
from strategy.strategy import Strategy

FPS = 60


def run_game():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')

    run = True
    clock = pygame.time.Clock()
    game = Game()
    interface = GUI(window, game)

    while run == True:
        clock.tick(FPS)

        if game.turn == YELLOW:
            score, new_board = Strategy.minimax(game.board, 3, YELLOW)
            game.ai_move(new_board)

        if game.winner() is not None:
            interface.end_game(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = interface.get_row_col_from_mouse(pos)
                game.select(row, col)

        if game.winner() is None:
            interface.update()

    pygame.quit()

def run_ui():
    game = Game()
    console = UI(game)
    run = True
    while run == True:
        if game.turn == YELLOW:
            score, new_board = Strategy.minimax(game.board, 3, YELLOW)
            game.ai_move(new_board)
            console.update()

        if game.winner() is not None:
            console.end_game(game.winner())
            return

        try:
            source_row, source_col = console.get_input_source()
            game.select(source_row, source_col)
            dest_row, dest_col = console.get_input_dest()
            if console.check_valid_move(dest_row, dest_col) == True:
                game.select(dest_row, dest_col)
            else:
                print("Invalid move! Try Again!")
        except ValueError as ve:
            print(str(ve))
        except GameException as ge:
            print(str(ge))

        if game.winner() is None:
            console.update()

def run_tests():
    test_all.roll()

if __name__ == "__main__":
    run_game()
    #run_ui()
    #run_tests()