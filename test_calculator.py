import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(5, 8), 13)



    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,3), 2)
        self.assertEqual(sub(-5,-2), -3)
        self.assertEqual(sub(5,0), 5)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(div(0,5),ZeroDivisionError)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(5,5), 1)
        self.assertEqual(log(2,8), 3)
        self.assertEqual(log(2,16), 4)

    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(log(0,0),ValueError)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()