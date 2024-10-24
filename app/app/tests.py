""" Sample test """
from django.test import TestCase
from app import calc


class CalcTests(TestCase):
    """ Test calc module """

    def test_add_numbers(self):
        """ Test that two numbers are added together """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Test that two numbers are subtracted """
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)
