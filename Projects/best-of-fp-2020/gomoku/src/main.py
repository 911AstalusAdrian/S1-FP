from service.strategy import AIStrategy
from service.game import Game
from service.settings import Settings
from ui.ui import UI
from ui.gui import GUI


if __name__ == "__main__":
    settings = Settings()
    settings.parse("settings.properties")
    strategy = AIStrategy()

    if settings["strategy"] == "easy":
        strategy = AIStrategy("easy")
    elif settings["strategy"] == "hard":
        strategy = AIStrategy("hard")
    elif settings["strategy"] == "extreme":
        strategy = AIStrategy("extreme")

    game = Game(strategy, 15, 15)

    if settings["ui"] == "ui":
        ui = UI(game)
        ui.run()
    elif settings["ui"] == "gui":
        gui = GUI(game)
        gui.run()
