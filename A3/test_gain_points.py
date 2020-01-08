from unittest import TestCase
from A3.movement import gain_points


class TestGainPoints(TestCase):
    def test_gain_points_zero(self):
        user_dict = {'Energy': 0}
        gain_points(user_dict)
        self.assertEqual({'Energy': 2}, user_dict)

    def test_gain_points_eight(self):
        user_dict = {'Energy': 8}
        gain_points(user_dict)
        self.assertEqual({'Energy': 10}, user_dict)

    def test_gain_points_nine(self):
        user_dict = {'Energy': 9}
        gain_points(user_dict)
        self.assertEqual({'Energy': 10}, user_dict)

    def test_gain_points_ten(self):
        user_dict = {'Energy': 10}
        gain_points(user_dict)
        self.assertEqual({'Energy': 10}, user_dict)
