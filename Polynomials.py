#!/usr/bin/env python
# Written by: DGC

# python imports
import unittest

# local imports

#==============================================================================
class Polynomial(object):
    
    def __init__(self, polynomial_as_string, var="x"):
        """\
        Pass in a polynomial as a string, e.g. "x^2 - 2*x + 4"

        keyword argument var is the variable used for these polynomials.\
        """
        self.coefficients = dict()
        self.var = var
        self.parse_polynomial_string(polynomial_as_string)

    def parse_polynomial_string(self, polynomial_as_string):
        poly_list = polynomial_as_string.split()
        for item in poly_list:
            if (not item in ("-", "+")):
                split_list = item.split(self.var)
                if (len(split_list) == 2):
                    # it's a power of x, so it should be 
                    # ["coefficient", "power"]
                    coefficient, power = split_list
                    if not power:
                        # it's x^1
                        power = 1
                    else:
                        power = int(power[1:])
                    coefficient = float(coefficient.rstrip("*"))
                    self.coefficients[power] = coefficient

    def __getitem__(self, index):
        """\
        This is used to get the index'th coefficient of the polynomial.\
        """
        return self.coefficients[index]

#==============================================================================
class utest_Polynomials(unittest.TestCase):
    
    def test_parser(self):
        p1 = Polynomial("1x^2 - 2*x + 4")
        self.assertEqual(p1[2], 1, "Coefficent of x^2 is not 1")
        self.assertEqual(p1[1], -2, "Coefficent of x is not -2")

#==============================================================================
if (__name__ == "__main__"):
    unittest.main(verbosity=2)
