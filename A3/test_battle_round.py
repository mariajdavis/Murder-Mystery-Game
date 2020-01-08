import io
from unittest import TestCase
from unittest.mock import patch
from A3.interaction import battle_round


class TestBattleRound(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.create_family_character', side_effect=[{'Energy': 5, 'Name': 'Sam Silver'}])
    def test_battle_round_user_loses(self, mock, mock_stdout):
        battle_round({'Energy': 0})
        actual = mock_stdout.getvalue()
        expected = "\nOh no, it's Sam Silver...\n\n" \
                   "They live here so you let them speak first...\n\n" \
                   "Sam Silver is persistent and painful and you lose all interest in the case.\n" \
                   "You secretly slink out the back entrance so the butler doesn't see that\n" \
                   "you've given up.\n\nGame over!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.create_family_character', side_effect=[{'Energy': 1, 'Name': 'Sam Silver'}])
    def test_battle_round_user_wins(self, mock, mock_stdout):
        battle_round({'Energy': 10})
        actual = mock_stdout.getvalue()
        expected = "\nOh no, it's Sam Silver...\n\n" \
                   "They live here so you let them speak first...\n\n" \
                   "Luckily, you bored Sam Silver and they walked away.\n"
        self.assertEqual(expected, actual)