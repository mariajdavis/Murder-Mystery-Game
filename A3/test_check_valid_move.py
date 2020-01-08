import io
from unittest import TestCase
from unittest.mock import patch
from A3.movement import check_valid_move


class TestCheckValidMove(TestCase):
    def test_check_valid_move_true_zeros(self):
        self.assertTrue(check_valid_move([0, 0]))

    def test_check_valid_move_true(self):
        self.assertTrue(check_valid_move([6, 4]))

    def test_check_valid_move_negative_num(self):
        self.assertFalse(check_valid_move([-1, 0]))

    def test_check_valid_move_num_too_large(self):
        self.assertFalse(check_valid_move([2, 10]))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_valid_move_false_negative_output(self, mock_stdout):
        check_valid_move([-1, 0])
        self.assertEqual("\nThat's out of bounds.\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_valid_move_false_too_large_output(self, mock_stdout):
        check_valid_move([10, 16])
        self.assertEqual("\nThat's out of bounds.\n", mock_stdout.getvalue())
