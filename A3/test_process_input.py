import io
from unittest import TestCase
from unittest.mock import patch
from A3.movement import process_input


class TestProcessInput(TestCase):
    @patch('A3.interaction.meet_family', return_value=False)
    def test_process_input_n(self, mock):
        user_dict = {'Position': [0, 0], 'Energy': 5}
        self.assertTrue(process_input('n', user_dict))

    @patch('A3.interaction.meet_family', return_value=False)
    def test_process_input_e(self, mock):
        user_dict = {'Position': [2, 2], 'Energy': 5}
        self.assertTrue(process_input('e', user_dict))

    @patch('A3.interaction.meet_family', return_value=False)
    def test_process_input_s(self, mock):
        user_dict = {'Position': [4, 4], 'Energy': 5}
        self.assertTrue(process_input('s', user_dict))

    @patch('A3.interaction.meet_family', return_value=False)
    def test_process_input_w(self, mock):
        user_dict = {'Position': [6, 6], 'Energy': 5}
        self.assertTrue(process_input('w', user_dict))

    @patch('A3.interaction.meet_family', return_value=False)
    def test_process_input_el(self, mock):
        user_dict = {'Position': [8, 8], 'Energy': 5}
        self.assertTrue(process_input('el', user_dict))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.meet_family', return_value=False)
    def test_process_input_el_output(self, mock1, mock_stdout):
        user_dict = {'Position': [8, 8], 'Energy': 5}
        process_input('el', user_dict)
        self.assertEqual("\nYou have 5 out of 10 energy remaining.\n", mock_stdout.getvalue())

    @patch('A3.interaction.meet_family', return_value=False)
    def test_process_input_quit(self, mock):
        user_dict = {'Position': [8, 8], 'Energy': 5}
        self.assertFalse(process_input('quit', user_dict))