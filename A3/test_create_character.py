from unittest import TestCase
from A3.game_driver import create_character


class TestCreateCharacter(TestCase):
    def test_create_character_equal(self):
        expected_value = {'Energy': 10, 'Position': [8, 4],
                      'Family': ['Laura Silver', 'Frederick Silver', 'Josephine Silver', 'Olivia Silver',
                               'Timothy Silver', 'Jack Silver', 'Melissa Silver', 'Sam Silver'],
                      'Staff': ['the cook', 'the laundry maid', 'the nurse', 'the valet', 'the stable boy',
                                'the barmaid'],
                      'Clues': ['Sarah Silver did it! I saw her murder Sir Silver!',
                                'Sir Silver was murdered by a knife from the kitchen!',
                                'Sir Silver was murdered in the cellar!'],
                      'Solution': 0}
        self.assertEqual(expected_value, create_character())

    def test_create_character_not_equal(self):
        expected_value = {'Energy': 0, 'Position': None,
                      'Family': ['none'],
                      'Staff': ['none'],
                      'Clues': ['none'],
                      'Solution': 0}
        self.assertNotEqual(expected_value, create_character())