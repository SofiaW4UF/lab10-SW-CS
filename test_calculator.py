#https://github.com/SofiaW4UF/lab10-SW-CS
#Partner 1: Sofia Wangensteen
#Partner 2: Chris Steele

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(5, 8), 13)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,3), 2)
        self.assertEqual(subtract(-5,-2), -3)
        self.assertEqual(subtract(5,0), 5)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(3, 7), 21)
        self.assertEqual(mul(5, 9), 45)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(16, 16), 1)
        self.assertEqual(div(4, 16), 4)
        self.assertEqual(div(3, 9), 3)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(5,5), 1)
        self.assertEqual(logarithm(2,8), 3)
        self.assertEqual(logarithm(2,16), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(4, 3), 5.0)
        self.assertEqual(hypotenuse(8, 6), 10.0)
        self.assertEqual(hypotenuse(16, 12), 20.0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(16), 4)

if __name__ == "__main__":
    unittest.main()