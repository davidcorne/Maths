#!/usr/bin/env python
# Written by: DGC

import copy

#==============================================================================
class BaseMatrix(object):
    
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

    @classmethod
    def FromRows(cls, lists, x=None, y=None):
        """
        Takes a list of rows which are read into the matrix.

        This creates an x by y matrix if given, otherwise it uses the 
        dimensions from the lists/
        
        This takes a list of rows so you can define a matrix naturally like 
        this:
        
        m = Matrix.FromRows(
            [
                [1, 2, 3],
                [2, 3, 4],
                [3, 4, 5],
                ]
            )

        This makes
        1 2 3
        2 3 4
        3 4 5

        but this

        m = Matrix.FromRows(
            [
                [1, 2, 3],
                [2, 3, 4],
                [3, 4, 5],
                ],
            4, 4
            )

        makes
        1 2 3 0
        2 3 4 0
        3 4 5 0
        0 0 0 0

        m = Matrix.FromRows(
            [
                [1, 2, 3],
                [2, 3, 4, 5],
                [3, 4, 5],
                ]
            )

        makes
        1 2 3 0
        2 3 4 5
        3 4 5 0
        """
        # find the biggest row
        new_x = 0
        for row in lists:
            if (len(row) > new_x):
                new_x = len(row)
        if (x is None):
            x = new_x
        elif (x < new_x):
            raise TypeError("values outside x range")
        new_y = len(lists)

        if (y is None):
            y = new_y
        elif (y < new_y):
            raise TypeError("values outside y range")

        m = cls(x, y)
        for i, row in enumerate(lists):
            for j, value in enumerate(row):
                m[j][i] = value
        return m

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

    def __copy__(self):
        m = Matrix(self.x, self.y)
        for i in range(self.x):
            for j in range(self.y):
                m[i][j] = self[i][j]
        return m
        
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
class Matrix(BaseMatrix):
    
    def __new__(cls, *arguments, **keyword_arguments):
        if (len(arguments) >= 2 and arguments[0] == arguments[1]):
            instance = object.__new__(SquareMatrix)
            instance.__init__(
                arguments[0],
                *arguments[2:],
                **keyword_arguments
                )
        else:
            instance = object.__new__(cls)
        return instance

#==============================================================================
class SquareMatrix(BaseMatrix):

    def __init__(self, size, assignment=lambda a,b: 0):
        super(SquareMatrix, self).__init__(size, size, assignment)

    def determinant(self):
        return 0
    
    def singular(self):
        return self.determinant() == 0

#==============================================================================
class IdentityMatrix(SquareMatrix):

    def __init__(self, size):
        super(IdentityMatrix, self).__init__(size, lambda a,b: int(a==b))

#==============================================================================
class RowVector(BaseMatrix):
    
    def __init__(self, columns, assignment=lambda a: 0):
        super(RowVector, self).__init__(columns, 1, lambda a,b: assignment(a))

#==============================================================================
class ColumnVector(BaseMatrix):
    
    def __init__(self, rows, assignment=lambda a: 0):
        super(ColumnVector, self).__init__(1, rows, lambda a,b: assignment(b))

#==============================================================================
if (__name__ == "__main__"):
    pass
