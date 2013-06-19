#!/usr/bin/env python
# Written by: DGC

# python imports
import unittest

# local imports
from matrix import *

#==============================================================================
class utest_Matrix(unittest.TestCase):
    
    def test_add(self):
        A = Matrix(1, 2)
        A[0][0] = 5
        B = Matrix(1, 2)
        expected_result = Matrix(1, 2)
        expected_result[0][0] = 5
        C = A + B
        self.assertEqual(expected_result[0][0], C[0][0])
        E = Matrix(1, 1)
        self.assertRaises(TypeError, lambda : A + E)

        A += A
        self.assertEqual(A[0][0], 10)
        self.assertEqual(A[0][1], 0)

    def test_sub(self):
        A = Matrix(4, 2)
        A[3][0] = 5
        B = Matrix(4, 2)
        expected_result = Matrix(4, 2)
        expected_result[3][0] = -5
        C = B - A
        self.assertEqual(C[3][0], expected_result[3][0])
        E = Matrix(1, 1)
        self.assertRaises(TypeError, lambda : A + E)

        A -= A
        # B is all zero, so A - A == B
        self.assertEqual(A, B)

    def test_eq(self):
        A = Matrix(3, 5)
        B = Matrix(3, 5)
        self.assertEqual(A, B)
        A[0][0] = 1
        self.assertNotEqual(A, B)

    def test_special_assignment(self):
        A = Matrix(5, 5, lambda a, b: a + b)
        for i in range(5):
            for j in range(5):
                self.assertEqual(A[i][j], i + j)

#==============================================================================
if (__name__ == "__main__"):
    unittest.main(verbosity=2)
