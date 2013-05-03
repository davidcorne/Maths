#!/usr/bin/env python
# Written by: DGC

# python imports
import unittest

# local imports

#==============================================================================
class PolynomialParserException(Exception):
    pass

#==============================================================================
class Polynomial(object):
    
    def __init__(self, polynomial_as_string, var="x"):
        """\
        Pass in a polynomial as a string, e.g. "x^2 - 2*x + 4"

        keyword argument var is the variable used for these polynomials.\
        """
        self.coefficients = dict()
        self.parse_polynomial_string(polynomial_as_string, var)

    def parse_polynomial_string(self, polynomial_as_string, var):
        poly_list = polynomial_as_string.split()
        sign = 1
        for item in poly_list:
            if (item in ("-", "+")):
                sign = int(item + "1")
            else:
                split_list = item.split(var)
                power = None
                coefficient = None
                if (len(split_list) == 2):
                    # it's a power of x, so it should be 
                    # ["coefficient", "power"]
                    coefficient, power = split_list
                    if not power:
                        # it's x^1
                        power = 1
                    else:
                        power = int(power[1:])
                    if not coefficient:
                        # it's x^1
                        coefficient = 1
                        sign = 1
                    else:
                        coefficient = sign * float(coefficient.rstrip("*"))
                elif (len(split_list) == 1):
                    # it's the constant
                    power = 0
                    coefficient = sign * float(split_list[0])
                else:
                    raise PolynomialParserException
                # add the coefficients if they already exist
                self.coefficients.setdefault(power, 0)
                self.coefficients[power] += coefficient
                
    def __getitem__(self, index):
        """\
        This is used to get the index'th coefficient of the polynomial.\
        """
        return self.coefficients[index]

    def __eq__(self, other):
        equal = True
        if (self.coefficients != other.coefficients):
            # there may be coefficients which are 0, returns a false not equal
            self_set = set(self.coefficients.keys())
            other_set = set(other.coefficients.keys())
            in_self = self_set - other_set
            if (in_self):
                # keys in self not in other
                for power in in_self:
                    if (self[power] != 0):
                        equal = False
            not_in_self = other_set - self_set
        return equal

    def __ne__(self, other):
        return not self == other

#==============================================================================
class utest_Polynomials(unittest.TestCase):
    
    def test_parser(self):
        p1 = Polynomial("x^2 - 2*x + 4")
        self.assertEqual(p1[2], 1, "Coefficent of x^2 is not 1")
        self.assertEqual(p1[1], -2, "Coefficent of x is not -2")
        self.assertEqual(p1[0], 4, "Constant is not 4")

        self.assertRaises(
            PolynomialParserException,
            Polynomial,
            "x^2x"
            )

        p2 = Polynomial("x^2 + x^2")
        self.assertEqual(p2[2], 2, "Parser does not add coefficients")

    def test_equality(self):
        p1 = Polynomial("x^8 + 1")
        p2 = Polynomial("x^8 + 1")
        p3 = Polynomial("x^7 + 1")
        self.assertEqual(p1, p2, "Equality fails.")
        self.assertEqual(p1, p2, "Equality fails.")
        self.assertNotEqual(p1, p3, "Inequality fails")
        self.assertNotEqual(p2, p3, "Inequality fails")

        # a trap!
        p4 = Polynomial("x^8 + 0x + 1")
        self.assertEqual(p1, p4, "Equality doesn't recognise 0")
        self.assertEqual(p4, p1, "Equality doesn't recognise 0")

#==============================================================================
if (__name__ == "__main__"):
    unittest.main(verbosity=2)
