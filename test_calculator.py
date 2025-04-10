

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-4, 9), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-2, -3), -5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(-2, -3), 1)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(5, 0), 5)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        try:
            div(0,5)
            self.fail("expected ZeroDivisionError not raised")
        except ZeroDivisionError:
            pass

    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10,100), 2)
        self.assertEqual(round(log(2, 8), 2), 3.00)
        self.assertEqual(round(log(5, 25), 2), 2.00)


    def test_log_invalid_base(self): # 1 assertion
        try:
            log(1,10)
            self.fail("expected ValueError not raised")
        except ValueError:
            pass
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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