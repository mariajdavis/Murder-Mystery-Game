import io
from unittest import TestCase
from unittest.mock import patch
from A3.game_driver import driver


class TestDriver(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.movement.process_input', side_effect=False)
    @patch('A3.movement.validate_input', return_value=False)
    @patch('builtins.input', return_value='hi')
    def test_driver_not_valid(self, mock1, mock2, mock3, mock_stdout):
        driver({'Position': [0, 0], 'Energy': 5, 'Solution': 2, 'Staff': []}, True)
        actual = mock_stdout.getvalue()
        expected = "\nChoose your next move...\n(n) north, (e) east, (s) south, or (w) west?\n" \
                   "Check your (el) energy level or (quit) at anytime!\nNot a valid option... try again.\n"
        self.assertEqual(expected, actual)

    class TestDriver(TestCase):
        @patch('sys.stdout', new_callable=io.StringIO)
        @patch('A3.movement.process_input', side_effect=True)
        @patch('A3.movement.validate_input', return_value=True)
        @patch('builtins.input', return_value='n')
        def test_driver_not_valid(self, mock1, mock2, mock3, mock_stdout):
            driver({'Position': [0, 0], 'Energy': 5, 'Solution': 2, 'Staff': []}, True)
            actual = mock_stdout.getvalue()
            expected = "..."
            self.assertEqual(expected, actual)

