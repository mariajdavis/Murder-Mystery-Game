from unittest import TestCase

from A3.movement import validate_input


class TestValidateInput(TestCase):
    def test_validate_input_north(self):
        self.assertTrue(validate_input('n'))

    def test_validate_input_east(self):
        self.assertTrue(validate_input('e'))

    def test_validate_input_south(self):
        self.assertTrue(validate_input('s'))

    def test_validate_input_west(self):
        self.assertTrue(validate_input('w'))

    def test_validate_input_energy_level(self):
        self.assertTrue(validate_input('el'))

    def test_validate_input_quit(self):
        self.assertTrue(validate_input('quit'))

    def test_validate_input_empty_string(self):
        self.assertFalse(validate_input(''))

    def test_validate_input_int(self):
        self.assertRaises(AttributeError, validate_input, 1)

    def test_validate_input_other_string(self):
        self.assertFalse(validate_input('h'))


