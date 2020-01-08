import io
from unittest import TestCase
from unittest.mock import patch
from A3.interaction import attack


class TestAttack(TestCase):
    @patch('A3.interaction.roll_die', side_effect=[5, 5])
    def test_attack_user_wins(self, mock):
        self.assertEqual([5, 0], attack({'Energy': 10}, {'Name': 'Sam Silver', 'Energy': 5}))

    @patch('A3.interaction.roll_die', side_effect=[5, 4])
    def test_attack_no_one_defeated(self, mock):
        self.assertEqual([5, 1], attack({'Energy': 10}, {'Name': 'Sam Silver', 'Energy': 5}))

    @patch('A3.interaction.roll_die', side_effect=[4])
    def test_attack_user_defeated(self, mock):
        self.assertEqual([0, 5], attack({'Energy': 3}, {'Name': 'Sam Silver', 'Energy': 5}))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.roll_die', side_effect=[5, 5])
    def test_attack_user_wins_output(self, mock, mock_stdout):
        attack({'Energy': 10}, {'Name': 'Sam Silver', 'Energy': 5})
        self.assertEqual('Luckily, you bored Sam Silver and they walked away.\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.roll_die', side_effect=[5, 4])
    def test_attack_no_one_defeated_output(self, mock, mock_stdout):
        attack({'Energy': 10}, {'Name': 'Sam Silver', 'Energy': 5})
        self.assertEqual('', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.roll_die', side_effect=[5])
    def test_attack_user_defeated_output(self, mock, mock_stdout):
        attack({'Energy': 4}, {'Name': 'Sam Silver', 'Energy': 5})
        self.assertEqual('', mock_stdout.getvalue())