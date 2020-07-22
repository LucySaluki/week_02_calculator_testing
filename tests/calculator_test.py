
import unittest
from src.calculator import add, divide, multiply, subtract #import everything you want to test

class TestCalculator(unittest.TestCase):
    def test_add(self):
    # arrange - addfunction is already, nothing to instantiate expected = 5
    # act - call the add function passing 2 and 3 to get result
    # assert - expect the result to be 5
        self.assertEqual(5, add(2, 3))

    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))

    def test_divide(self):
        self.assertEqual(2, divide(4, 2))

    def test_multiply(self):
        self.assertEqual(12, multiply(4, 3))