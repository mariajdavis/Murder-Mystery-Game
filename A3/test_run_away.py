import io
from unittest import TestCase
from unittest.mock import patch
from A3.interaction import run_away, roll_die


class TestRunAway(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.roll_die', side_effect=[3])
    @patch('random.randint', return_value=1)
    def test_run_away(self, mock1, mock2, mock_stdout):
        run_away({'Energy': 5})
        self.assertEqual("\nIn your rush running away, you lost 3 energy points!\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('A3.interaction.roll_die', side_effect=[4])
    @patch('random.randint', return_value=1)
    def test_run_away(self, mock1, mock2, mock_stdout):
        run_away({'Energy': 4})
        self.assertEqual("\nIn your rush running away, you lost 4 energy points!\n", mock_stdout.getvalue())

    @patch('random.randint', return_value=2)
    def test_run_away_none_2(self, mock1):
        self.assertIsNone(run_away({'Energy': 4}))

    @patch('random.randint', return_value=3)
    def test_run_away_none_3(self, mock1):
        self.assertIsNone(run_away({'Energy': 4}))

    @patch('random.randint', return_value=4)
    def test_run_away_none_4(self, mock1):
        self.assertIsNone(run_away({'Energy': 4}))

    @patch('A3.interaction.roll_die', side_effect=[4])
    @patch('random.randint', return_value=1)
    def test_run_away_4_energy_points_lost(self, mock1, mock2):
        char_dict = {'Energy': 4}
        run_away(char_dict)
        self.assertEqual({'Energy': 0}, char_dict)

        @patch('A3.interaction.roll_die', side_effect=[1])
        @patch('random.randint', return_value=1)
        def test_run_away_1_energy_point_lost(self, mock1, mock2):
            char_dict = {'Energy': 4}
            run_away(char_dict)
            self.assertEqual({'Energy': 3}, char_dict)