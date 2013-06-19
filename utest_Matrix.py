#!/usr/bin/env python
# Written by: DGC

# python imports
import unittest

# local imports
from matrix import *

#==============================================================================
class utest_Matrix(unittest.TestCase):
    
    def test_ctor(self):
        self.assertRaises(TypeError, Matrix, -1, -1)

    def test_add(self):
        A = Matrix(1, 2)
        A[0][0] = 5
        B = Matrix(1, 2)
        expected_result = Matrix(1, 2)
        expected_result[0][0] = 5
        C = A + B
        self.assertEqual(expected_result, C)
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

    def test_mul(self):
        A = SquareMatrix(3, lambda a,b: a+b)
        B = SquareMatrix(3, lambda a,b: a)
        # 0 1 2   0 1 2    0 3 6
        # 1 2 3 * 0 1 2 == 0 6 12
        # 2 3 4   0 1 2    0 9 18
        expected_result = SquareMatrix(3)
        expected_result[1][0] = 3
        expected_result[1][1] = 6
        expected_result[1][2] = 9
        expected_result[2][0] = 6
        expected_result[2][1] = 12
        expected_result[2][2] = 18
        
        self.assertEqual(A * B, expected_result)
        self.assertNotEqual(B * A, expected_result)
        
        new_A = Matrix(3, 3, lambda a,b: a+b)
        self.assertEqual(A, new_A)
        self.assertEqual(new_A * B, expected_result)
        
        # cross dimension multiply
        C = Matrix(3, 5, lambda a,b: a+b)
        D = Matrix(1, 3, lambda a,b: b)
        expected_result = Matrix(1, 5)
        expected_result[0][0] = 5
        expected_result[0][1] = 8
        expected_result[0][2] = 11
        expected_result[0][3] = 14
        expected_result[0][4] = 17

        self.assertEqual(C * D, expected_result)

        self.assertRaises(TypeError, lambda : D * C)
        
        I = IdentityMatrix(3)
        self.assertEqual(I * A, A)
        self.assertEqual(A * I, A)
        
        J = IdentityMatrix(3)
        I *= I
        self.assertEqual(I, J)

    def test_pow(self):
        I = IdentityMatrix(5)
        J = I ** 20
        self.assertEqual(I, J)

        m = Matrix(2, 2)
        m[0][0] = 1
        m[0][1] = 2
        m[1][0] = 2
        m[1][1] = 1

        square = Matrix(2, 2)
        square[0][0] = 5
        square[0][1] = 4
        square[1][0] = 4
        square[1][1] = 5
        
        self.assertEqual(m * m, m ** 2)
        self.assertEqual(m ** 2, square)

        cube = Matrix(2, 2)
        cube[0][0] = 13
        cube[0][1] = 14
        cube[1][0] = 14
        cube[1][1] = 13

        self.assertEqual(m * m * m, m ** 3)
        self.assertEqual(m ** 3, cube)

#==============================================================================
class utest_SquareMatrix(unittest.TestCase):

    def test_ctor(self):
        m = Matrix(3, 3)
        self.assertIsInstance(m, SquareMatrix)
        m = Matrix(3, 5)
        self.assertNotIsInstance(m, SquareMatrix)
        # one argument should be a type error not a range error
        self.assertRaises(TypeError, Matrix, 5)

#==============================================================================
if (__name__ == "__main__"):
    unittest.main(verbosity=2)
