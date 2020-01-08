from unittest import TestCase

from A3.interaction import create_family_character


class TestCreateFamilyCharacter(TestCase):
    def test_create_family_character_family_names(self):
        char_dict = {'Family': ['Sam Silver', 'Melissa Silver']}
        self.assertEqual({'Name': 'Sam Silver', 'Energy': 5}, create_family_character(char_dict))

    def test_create_family_character_different_name(self):
        char_dict = {'Family': ['Simon', 'Maria']}
        self.assertEqual({'Name': 'Simon', 'Energy': 5}, create_family_character(char_dict))

    def test_create_family_character_empty_list(self):
        char_dict = {'Family': []}
        self.assertRaises(IndexError, create_family_character, char_dict)