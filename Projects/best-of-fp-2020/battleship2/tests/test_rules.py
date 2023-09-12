from random import randint
from unittest import TestCase

from errors import RuleError
from persistence.rules import Rules


class TestRules(TestCase):

    def setUp(self) -> None:
        self.__original_edge = Rules().edge
        self.__original_can_touch = Rules().can_touch
        self.__original_number_of_a = Rules().number_of['carrier']
        self.__original_number_of_b = Rules().number_of['battleship']
        self.__original_number_of_c = Rules().number_of['cruiser']
        self.__original_number_of_d = Rules().number_of['destroyer']
        self.__original_number_of_s = Rules().number_of['submarine']
        self.__original_difficulty = Rules().difficulty
        self.__original_display_probability = Rules().display_probability
        self.__original_test = Rules().test

        Rules().set_rules(
            edge=10,
            can_touch=True,
            carriers=1,
            battleships=1,
            cruisers=1,
            destroyers=1,
            submarines=1,
            difficulty=2,
            display_probability=True,
            test=False
        )

    def test_edge(self):
        self.assertEqual(Rules().edge, 10)
        with self.assertRaisesRegex(RuleError, '^.*edge.*$'):
            Rules().set_rules(edge=13)
        with self.assertRaisesRegex(RuleError, '^.*edge.*$'):
            Rules().set_rules(edge='asda')
        with self.assertRaisesRegex(RuleError, '^.*edge.*$'):
            Rules().set_rules(edge=False)

        self.assertEqual(Rules().edge, 10)
        Rules().set_rules(edge=15)
        self.assertEqual(Rules().edge, 10)
        Rules().set_rules(edge=20)
        self.assertEqual(Rules().edge, 10)

    def test_can_touch(self):
        self.assertTrue(Rules().can_touch)
        with self.assertRaisesRegex(RuleError, '^.*touch.*$'):
            Rules().set_rules(can_touch=15)
        with self.assertRaisesRegex(RuleError, '^.*touch.*$'):
            Rules().set_rules(can_touch='asda')

        self.assertTrue(Rules().can_touch)
        Rules().set_rules(can_touch=False)
        self.assertFalse(Rules().can_touch)

    def test_number_of(self):
        self.assertEqual(Rules().number_of['carrier'], 1)
        self.assertEqual(Rules().number_of['battleship'], 1)
        self.assertEqual(Rules().number_of['cruiser'], 1)
        self.assertEqual(Rules().number_of['destroyer'], 1)
        self.assertEqual(Rules().number_of['submarine'], 1)

        with self.assertRaisesRegex(RuleError, '^.*number of destroyers.*$'):
            Rules().set_rules(destroyers='asd')
        with self.assertRaisesRegex(RuleError, '^.*number of submarines.*$'):
            Rules().set_rules(submarines=randint(-10, 0))
        with self.assertRaisesRegex(RuleError, '^.*number of battleships.*$'):
            Rules().set_rules(battleships=randint(6, 15))
        with self.assertRaisesRegex(RuleError, '^.*number of carriers.*$'):
            Rules().set_rules(carriers=randint(-10, 0))
        with self.assertRaisesRegex(RuleError, '^.*number of cruisers.*$'):
            Rules().set_rules(cruisers=True)

        Rules().set_rules(
            carriers=2,
            battleships=4,
            cruisers=5,
            destroyers=2,
            submarines=3
        )
        self.assertEqual(Rules().number_of['carrier'], 1)
        self.assertEqual(Rules().number_of['battleship'], 1)
        self.assertEqual(Rules().number_of['cruiser'], 1)
        self.assertEqual(Rules().number_of['destroyer'], 1)
        self.assertEqual(Rules().number_of['submarine'], 1)

    def test_difficulty(self):
        self.assertEqual(Rules().difficulty, 2)
        with self.assertRaisesRegex(RuleError, '^.*difficulty.*$'):
            Rules().set_rules(difficulty=5)
        with self.assertRaisesRegex(RuleError, '^.*difficulty.*$'):
            Rules().set_rules(difficulty=0)
        with self.assertRaisesRegex(RuleError, '^.*difficulty.*$'):
            Rules().set_rules(difficulty='asda')
        with self.assertRaisesRegex(RuleError, '^.*difficulty.*$'):
            Rules().set_rules(difficulty=False)

        self.assertEqual(Rules().difficulty, 2)
        Rules().set_rules(difficulty=1)
        self.assertEqual(Rules().difficulty, 1)
        Rules().set_rules(difficulty=3)
        self.assertEqual(Rules().difficulty, 3)
        Rules().set_rules(difficulty=4)
        self.assertEqual(Rules().difficulty, 4)

    def test_display_probability(self):
        self.assertTrue(Rules().display_probability)
        with self.assertRaisesRegex(RuleError, '^.*display probability.*$'):
            Rules().set_rules(display_probability=15)
        with self.assertRaisesRegex(RuleError, '^.*display probability.*$'):
            Rules().set_rules(display_probability='asda')

        self.assertTrue(Rules().display_probability)
        Rules().set_rules(display_probability=False)
        self.assertFalse(Rules().display_probability)

    def test_test(self):
        self.assertFalse(Rules().test)
        with self.assertRaisesRegex(RuleError, '^.*test.*$'):
            Rules().set_rules(test=15)
        with self.assertRaisesRegex(RuleError, '^.*test.*$'):
            Rules().set_rules(test='asda')

        self.assertFalse(Rules().test)
        Rules().set_rules(test=True)
        self.assertTrue(Rules().test)

    def test_composed_errors(self):
        with self.assertRaisesRegex(RuleError, '^.*key.*$'):
            Rules().set_rules(difficult=5)
        with self.assertRaisesRegex(RuleError, '^.*touch.*\n.*submarines.*\n.*carriers.*\n.*battleships.*\n'
                                               '.*edge.*\n.*difficulty.*\n.*cruisers.*\n.*destroyers.*$\n'):
            Rules().set_rules(
                can_touch=123,
                submarines=-1,
                carriers=10,
                battleships='asd',
                edge=False,
                difficulty=5,
                cruisers=True,
                destroyers='ss'
            )

    def tearDown(self) -> None:
        Rules().set_rules(
            edge=self.__original_edge,
            can_touch=self.__original_can_touch,
            carriers=self.__original_number_of_a,
            battleships=self.__original_number_of_b,
            cruisers=self.__original_number_of_c,
            destroyers=self.__original_number_of_d,
            submarines=self.__original_number_of_s,
            difficulty=self.__original_difficulty,
            display_probability=self.__original_display_probability,
            test=self.__original_test
        )
