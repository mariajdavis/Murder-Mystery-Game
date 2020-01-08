import io
from unittest import TestCase
from unittest.mock import patch
from A3.interaction import meet_family


class TestMeetFamily(TestCase):
    @patch('builtins.input', side_effect=['s'])
    @patch('random.randint', return_value = 1)
    def test_meet_family_stay(self, mock1, mock2):
        self.assertTrue(meet_family({'Energy': 10}))

    @patch('random.randint', return_value = 2)
    def test_meet_family_none_2(self, mock1):
        self.assertIsNone(meet_family({'Energy': 10}))

    @patch('random.randint', return_value = 3)
    def test_meet_family_none_3(self, mock1):
        self.assertIsNone(meet_family({'Energy': 10}))

    @patch('random.randint', return_value = 4)
    def test_meet_family_none_4(self, mock1):
        self.assertIsNone(meet_family({'Energy': 10}))

    @patch('builtins.input', side_effect=['r'])
    @patch('random.randint', return_value=1)
    def test_meet_family_run_away(self, mock1, mock2):
        self.assertFalse(meet_family({'Energy': 10}))

    @patch('builtins.input', side_effect=['l', 'r'])
    @patch('random.randint', return_value=1)
    def test_meet_family_wrong_input_first(self, mock1, mock2):
        self.assertFalse(meet_family({'Energy': 10}))

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['r'])
    @patch('random.randint', return_value=1)
    def test_meet_family_run_away_print(self, mock1, mock2, mock_stdout):
        meet_family({'Energy': 10})
        expected = "\nOh no... It's someone from the family.\n\nIn your rush running away, you lost 1 energy points!\n"
        self.assertEqual(expected, mock_stdout.getvalue())


