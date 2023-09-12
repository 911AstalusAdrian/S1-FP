from board.board import Board
from gameui.gamegui import GameGUI
from gameui.gameui import GameUI
from player.computer import Computer
from player.human import Human
from settings.settings import Settings, SettingsException
from strategy.minimaxstrategy import MinimaxStrategy
from strategy.randomstrategy import RandomStrategy


if __name__ == "__main__":
    BOARD_LENGTH = 6
    BOARD_HEIGHT = 7
    FIRST_PLAYER_VALUE = 1
    SECOND_PLAYER_VALUE = 2
    settings = Settings("../Data/settings.properties")
    try:
        board = Board(BOARD_LENGTH, BOARD_HEIGHT)
        if settings.first_player_type == "Human":
            first_player = Human(settings.first_player_name, board, FIRST_PLAYER_VALUE)
        elif settings.first_player_type == "Computer":
            if settings.first_player_ai == "Smart":
                first_player = Computer(settings.first_player_name, board, FIRST_PLAYER_VALUE, MinimaxStrategy())
            elif settings.first_player_ai == "Random":
                first_player = Computer(settings.first_player_name, board, FIRST_PLAYER_VALUE, RandomStrategy())
            else:
                raise SettingsException("Invalid AI type for the first player!")
        else:
            raise SettingsException("Invalid type for the first player!")
        if settings.second_player_type == "Human":
            second_player = Human(settings.second_player_name, board, SECOND_PLAYER_VALUE)
        elif settings.second_player_type == "Computer":
            if settings.second_player_ai == "Smart":
                second_player = Computer(settings.second_player_name, board, SECOND_PLAYER_VALUE, MinimaxStrategy())
            elif settings.second_player_ai == "Random":
                second_player = Computer(settings.second_player_name, board, SECOND_PLAYER_VALUE, RandomStrategy())
            else:
                raise SettingsException("Invalid AI type for the second player!")
        else:
            raise SettingsException("Invalid type for the second player!")
        if settings.ui_type == "Console":
            game = GameUI(board, first_player, second_player)
            game.play()
        elif settings.ui_type == "GUI":
            game = GameGUI(board, first_player, second_player)
        else:
            raise SettingsException("Invalid type for the ui!")
    except SettingsException as se:
        print(se, "Consult the settings file! Bye!")
