import io
from unittest import TestCase
from unittest.mock import patch
from A3.messages import game_over


class TestGameOver(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over(self, mock_stdout):
        game_over({'Energy': 2}, 'Frederick Silver')
        actual = mock_stdout.getvalue()
        expected = 'Frederick Silver is persistent and painful and you lose all interest in the case.\n'\
                 'You secretly slink out the back entrance so the butler doesn\'t see that\n'\
                 'you\'ve given up.\n\nGame over!\n'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_over(self, mock_stdout):
        game_over({'Energy': 0}, 'Sam Silver')
        actual = mock_stdout.getvalue()
        expected = 'Sam Silver is persistent and painful and you lose all interest in the case.\n'\
                 'You secretly slink out the back entrance so the butler doesn\'t see that\n'\
                 'you\'ve given up.\n\nGame over!\n'
        self.assertEqual(expected, actual)

