from unittest import TestCase
from unittest.mock import patch
from A3.interaction import roll_die


class TestRollDie(TestCase):
    @patch("random.randint", return_value = 1)
    def test_roll_die_ones(self, mock_roll):
        self.assertsEqual = (1, roll_die(1, 1))

    @patch("random.randint", return_value=2)
    def test_roll_die_0_sides(self, mock_roll):
        self.assertsEqual = (0, roll_die(2, 0))

    @patch("random.randint", return_value=3)
    def test_roll_die_0_rolls(self, mock_roll):
        self.assertsEqual = (0, roll_die(0, 3))

    @patch("random.randint", return_value=7)
    def test_roll_die_same_values(self, mock_roll):
        self.assertsEqual = (None, roll_die(6, 6))

    @patch("random.randint", return_value=5)
    def test_roll_die_zeros(self, mock_roll):
        self.assertsEqual = (0, roll_die(0, 0))

    @patch("random.randint", return_value=8)
    def test_roll_die_large(self, mock_roll):
        self.assertsEqual = (64, roll_die(8, 8))
