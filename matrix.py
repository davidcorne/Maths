#!/usr/bin/env python
# Written by: DGC

import copy

#==============================================================================
class Matrix(object):
    
    def __init__(self, x, y, assignment=lambda a,b: 0):
        """
        Creates an x by y matrix.
        
        The assignment options takes a function with two arguments. This 
        function defines what the defualt values of the matrix cells are.
        By default it fills the matrix with zeros.

        e.g 
        
        Matrix(3, 4, lambda a,b: a+b) gives

        0 1 2
        1 2 3
        2 3 4
        3 4 5

        Note, this is indexed from zero not one.
        """
        if (x < 1 or y < 1):
            raise TypeError("Matrix dimensions should be positive")
        self.x = x
        self.y = y
        self.matrix = []
        for i in range(self.x):
            column = []
            for j in range(self.y):
                column.append(assignment(i, j))
            self.matrix.append(column)

    def __repr__(self):
        out = []
        for j in range(self.y):
            row = []
            for i in range(self.x):
                row.append(repr(self.matrix[i][j]))
            out.append(" ".join(row))
        return "\n".join(out)

    def column(self, index):
        return copy.copy(self[index])

    def row(self, index):
        row = []
        for i in range(self.x):
            row.append(self.matrix[i][index])
        return row

    def __getitem__(self, key):
        """
        Returns the keyth column so that element (x, y) is accessed as 
        follows: Matrix[x][y]
        """
        return self.matrix[key]

    def dimensions(self):
        return (self.x, self.y)
    
    def element_wise_unary(self, operation):
        """
        This applies a unary function to this matrix returns a matrix of the
        results.
        """
        m = Matrix(self.x, self.y)
        for i in range(self.x):
            for j in range(self.y):
                m.matrix[i][j] = operation(self.matrix[i][j])
        return m

    def element_wise_binary(self, other, operation):
        """
        This applies a binary function to two matricies and returns a matrix
        of the results.
        """
        if (self.dimensions() != other.dimensions()):
            raise TypeError("Matrix dimensions do not match")
        m = Matrix(self.x, self.y)
        for i in range(self.x):
            for j in range(self.y):
                result = operation(self.matrix[i][j],  other.matrix[i][j])
                m.matrix[i][j] = result
        return m

    def square(self):
        return self.x == self.y

    def __eq__(self, other):
        equal = False
        if (self.dimensions() == other.dimensions()):
            equal = True
            for a, b in zip(self.matrix, other.matrix):
                if (a != b):
                    equal = False
        return equal

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __add__(self, other):
        return self.element_wise_binary(other, lambda a, b: a + b)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        return self - other

    def __sub__(self, other):
        return self.element_wise_binary(other, lambda a, b: a - b)

    def __imul__(self, other):
        return self * other

    def __mul__(self, other):
        if (self.x != other.y):
            raise TypeError("Matricies are wrong dimensions to multiply")
        m = Matrix(other.x, self.y)
        for i in range(other.x):
            for j in range(self.y):
                row = self.row(j)
                column = other.column(i)
                value = sum([a*b for a, b in zip(row, column)])
                m[i][j] = value
        return m
        
    def __pow__(self, power):
        if (not self.square() and power > 1):
            raise TypeError("Can only take powers of square matricies")
        m = self
        for i in range(power-1):
            m *= self
        return m

#==============================================================================
class SquareMatrix(Matrix):

    def __init__(self, size, assignment=lambda a,b: 0):
        super(SquareMatrix, self).__init__(size, size, assignment)

#==============================================================================
class IdentityMatrix(SquareMatrix):

    def __init__(self, size):
        super(IdentityMatrix, self).__init__(size, lambda a,b: int(a==b))

#==============================================================================
class RowVector(Matrix):
    
    def __init__(self, columns, assignment=lambda a: 0):
        super(RowVector, self).__init__(columns, 1, lambda a,b: assignment(a))

#==============================================================================
class ColumnVector(Matrix):
    
    def __init__(self, rows, assignment=lambda a: 0):
        super(ColumnVector, self).__init__(1, rows, lambda a,b: assignment(b))

#==============================================================================
if (__name__ == "__main__"):
    r = RowVector(5, lambda a: a)
    print r
    print ""
    v = ColumnVector(5, lambda a: a)
    print v
    print""
    print r * v
