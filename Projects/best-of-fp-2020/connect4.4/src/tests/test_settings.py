from unittest import TestCase

from settings.settings import Settings, SettingsException


class TestSettings(TestCase):
    def setUp(self):
        self.settings = Settings("../../Data/test_settings.properties")

    def test_first_player_type(self):
        self.assertEqual(self.settings.first_player_type, "Human")

    def test_first_player_name(self):
        self.assertEqual(self.settings.first_player_name, "Yellow")

    def test_first_player_ai(self):
        self.assertEqual(self.settings.first_player_ai, "")

    def test_second_player_type(self):
        self.assertEqual(self.settings.second_player_type, "Computer")

    def test_second_player_name(self):
        self.assertEqual(self.settings.second_player_name, "Red")

    def test_second_player_ai(self):
        self.assertEqual(self.settings.second_player_ai, "Smart")

    def test_ui_type(self):
        self.assertEqual(self.settings.ui_type, "GUI")


class TestSettingsException(TestCase):
    def test_init(self):
        settings_exception = SettingsException("Test message")
        self.assertEqual(str(settings_exception), "Test message")
