import configparser


class SettingsException(Exception):
    def __init__(self, message):
        """
        Creates an object of type SettingsException
        :param message: The message of the SettingsException, a string
        """
        super().__init__(message)


class Settings:
    def __init__(self, file_name):
        """
        Creates an object of type Settings
        :param file_name: The location of the file containing the settings
        """
        self.__file_name = file_name
        self.__load()

    def __load(self):
        """
        Reads the settings file and loads the settings into the program
        :return: nothing
        """
        config = configparser.ConfigParser()
        config.read(self.__file_name)
        self.__ui_type = config.get("DEFAULT", "ui_type").strip("\"")
        self.__first_player_type = config.get("DEFAULT", "first_player_type").strip("\"")
        self.__first_player_name = config.get("DEFAULT", "first_player_name").strip("\"")
        self.__first_player_ai = config.get("DEFAULT", "first_player_ai").strip("\"")
        self.__second_player_type = config.get("DEFAULT", "second_player_type").strip("\"")
        self.__second_player_name = config.get("DEFAULT", "second_player_name").strip("\"")
        self.__second_player_ai = config.get("DEFAULT", "second_player_ai").strip("\"")

    @property
    def first_player_type(self):
        """
        Returns the value of the first_player_type setting
        :return: The value of the first_player_type setting, a string
        """
        return self.__first_player_type

    @property
    def first_player_name(self):
        """
        Returns the value of the first_player_name setting
        :return: The value of the first_player_name setting, a string
        """
        return self.__first_player_name

    @property
    def first_player_ai(self):
        """
        Returns the value of the first_player_ai setting
        :return: The value of the first_player_ai setting, a string
        """
        return self.__first_player_ai

    @property
    def second_player_type(self):
        """
        Returns the value of the second_player_type setting
        :return: The value of the second_player_type setting, a string
        """
        return self.__second_player_type

    @property
    def second_player_name(self):
        """
        Returns the value of the second_player_name setting
        :return: The value of the second_player_name setting, a string
        """
        return self.__second_player_name

    @property
    def second_player_ai(self):
        """
        Returns the value of the second_player_ai setting
        :return: The value of the second_player_ai setting, a string
        """
        return self.__second_player_ai

    @property
    def ui_type(self):
        """
        Returns the value of the ui_type setting
        :return: The value of the ui_type setting, a string
        """
        return self.__ui_type
