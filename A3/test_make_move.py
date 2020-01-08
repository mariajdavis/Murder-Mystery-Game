import io
from unittest import TestCase
from unittest.mock import patch
from A3.movement import make_move


class TestMakeMove(TestCase):
    @patch('A3.interaction.meet_staff', return_value=False)
    @patch('A3.interaction.meet_family', return_value=False)
    @patch('A3.movement.check_valid_move', return_value=True)
    def test_make_move_valid(self, mock1, mock2, mock3):
        user_dict = {'Position': [0, 0], 'Energy': 10, 'Staff': []}
        make_move(user_dict, [1, 0])
        self.assertEqual([1, 0], user_dict['Position'])

    @patch('A3.movement.check_valid_move', return_value=False)
    def test_make_move_not_valid(self, mock1):
        user_dict = {'Position': [0, 0], 'Energy': 10, 'Staff': []}
        make_move(user_dict, [-1, 0])
        self.assertEqual([0, 0], user_dict['Position'])

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.meet_staff', return_value=False)
    @patch('A3.interaction.meet_family', return_value=False)
    @patch('A3.movement.check_valid_move', return_value=True)
    def test_make_move_valid_output(self, mock1, mock2, mock3, mock_stdout):
        user_dict = {'Position': [0, 0], 'Energy': 10, 'Staff': []}
        make_move(user_dict, [1, 0])
        self.assertEqual('\nYou are now in square [1, 0]\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.movement.check_valid_move', return_value=False)
    def test_make_move_not_valid_output(self, mock1, mock_stdout):
        user_dict = {'Position': [0, 0], 'Energy': 10, 'Staff': []}
        make_move(user_dict, [-1, 0])
        self.assertEqual('', mock_stdout.getvalue())