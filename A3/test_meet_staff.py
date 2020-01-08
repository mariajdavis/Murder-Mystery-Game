import io
from unittest import TestCase
from unittest.mock import patch
from A3.interaction import meet_staff


class TestMeetStaff(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value = 1)
    def test_meet_staff_no_clue(self, mock, mock_stdout):
        meet_staff({'Staff': ['the maid', 'the gardener'], 'Clues': ['weapon', 'location', 'criminal'], 'Solution': 0})
        expected = "\nOh look, it's the maid!\n\nThe maid: I heard the butler has you looking for clues! I'm sorry but I don't\n" \
                   "\t\t\thave anything for you. I have to get back to work. Good luck!\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value = 1)
    def test_meet_staff_find_clue(self, mock, mock_stdout):
        meet_staff({'Staff': ['the gardener', 'butler'], 'Clues': ['weapon', 'location', 'criminal'], 'Solution': 0})
        expected = "\nOh look, it's the gardener!\n\nThe gardener: You have to tell the Butler that criminal\n" \
                   "\t\t\tI have to go! Good luck!\n\nYou now have 1 out of 3 of the clues!\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value = 1)
    def test_meet_staff_empty_staff_list(self, mock, mock_stdout):
        meet_staff({'Staff': [], 'Clues': ['weapon', 'location', 'criminal'], 'Solution': 0})
        self.assertEqual('', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.randint', return_value = 1)
    def test_meet_staff_empty_clue_list(self, mock, mock_stdout):
        self.assertRaises(IndexError, meet_staff, {'Staff': ['the gardener'], 'Clues': [], 'Solution': 3})

    @patch('random.randint', return_value = 2)
    def test_meet_staff_none_2(self, mock):
        self.assertIsNone(meet_staff({}))

    @patch('random.randint', return_value = 2)
    def test_meet_staff_none_3(self, mock):
        self.assertIsNone(meet_staff({}))

    @patch('random.randint', return_value = 2)
    def test_meet_staff_none_4(self, mock):
        self.assertIsNone(meet_staff({}))