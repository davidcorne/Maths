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
        poly_list = polynomial_as_string.split()

    def __getitem__(self, index):
        """\
        This is used to get the index'th coefficient of the polynomial.\
        """
        return self.coefficients[index]

#==============================================================================
class utest_Polynomials(unittest.TestCase):
    
    def test_parser(self):
        p1 = Polynomial("x^2 - 2*x + 4")
        self.assertEqual(p1[2], 1, "Coefficent of x^1 is not 1")

#==============================================================================
if (__name__ == "__main__"):
    unittest.main(verbosity=2)
