from configparser import ConfigParser
from dataclasses import dataclass

from Interfaces.Console import Connect4UI
from Interfaces.GUI import Connect4GUI
from Strategies.MinimaxStrategy import MinimaxStrategy


@dataclass
class Settings:
    ui: str

    def __init__(self, file_name):
        settings = ConfigParser()
        settings.read(file_name)

        self.ui = settings.get('Settings', 'ui')


def main():
    settings = Settings('settings.properties')

    if settings.ui == "console":
        ui = Connect4UI(MinimaxStrategy)
        ui.run_menu()
    elif settings.ui == "GUI":
        ui = Connect4GUI(MinimaxStrategy)
        ui.run_menu()
    else:
        print("Error while loading settings.")


if __name__ == '__main__':
    main()
