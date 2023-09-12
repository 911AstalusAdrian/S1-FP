from unittest import TestCase

from persistence.last_board_config import LastBoardConfig


class TestLastBoardConfig(TestCase):

    def setUp(self) -> None:

        self._config = LastBoardConfig()
        self._initial_d_o = self._config.get_orientation('destroyer')
        self._initial_s_o = self._config.get_orientation('submarine')
        self._initial_c_o = self._config.get_orientation('cruiser')
        self._initial_b_o = self._config.get_orientation('battleship')
        self._initial_a_o = self._config.get_orientation('carrier')

        self._initial_d_p = self._config.get_position('destroyer')
        self._initial_s_p = self._config.get_position('submarine')
        self._initial_c_p = self._config.get_position('cruiser')
        self._initial_b_p = self._config.get_position('battleship')
        self._initial_a_p = self._config.get_position('carrier')

    def test_config(self):

        self._config.set_config(
            {'destroyer':   {'position': 'a1', 'orientation': 'horizontal'},
             'submarine':   {'position': 'c1', 'orientation': 'horizontal'},
             'cruiser':     {'position': 'e1', 'orientation': 'horizontal'},
             'battleship':  {'position': 'g1', 'orientation': 'horizontal'},
             'carrier':     {'position': 'j1', 'orientation': 'horizontal'}}
        )

        self.assertEqual(self._config.get_orientation('destroyer'), 'horizontal')
        self.assertEqual(self._config.get_orientation('submarine'), 'horizontal')
        self.assertEqual(self._config.get_orientation('cruiser'), 'horizontal')
        self.assertEqual(self._config.get_orientation('battleship'), 'horizontal')
        self.assertEqual(self._config.get_orientation('carrier'), 'horizontal')

        self.assertEqual(self._config.get_position('destroyer'), 'a1')
        self.assertEqual(self._config.get_position('submarine'), 'c1')
        self.assertEqual(self._config.get_position('cruiser'), 'e1')
        self.assertEqual(self._config.get_position('battleship'), 'g1')
        self.assertEqual(self._config.get_position('carrier'), 'j1')

    def tearDown(self) -> None:

        self._config.set_config(
            {'destroyer': {'position': self._initial_d_p, 'orientation': self._initial_d_o},
             'submarine': {'position': self._initial_s_p, 'orientation': self._initial_s_o},
             'cruiser': {'position': self._initial_c_p, 'orientation': self._initial_c_o},
             'battleship': {'position': self._initial_b_p, 'orientation': self._initial_b_o},
             'carrier': {'position': self._initial_a_p, 'orientation': self._initial_a_o}}
        )
