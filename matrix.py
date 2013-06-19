#!/usr/bin/env python
# Written by: DGC

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

        Note. this is indexed from zero not one.
        """
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

    def __getitem__(self, key):
        """
        Returns the keyth column so that element (x, y) is accessed as 
        follows: Matrix[x][y]
        """
        return self.matrix[key]

    def dimensions(self):
        return (self.x, self.y)
    
    def element_wise(self, other, operation):
        """
        This applies a binary function to two matricies and returns a matrix
        of the results
        """
        if (self.dimensions() != other.dimensions()):
            raise TypeError("Matrix dimensions do not match")
        m = Matrix(self.x, self.y)
        for i in range(self.x):
            for j in range(self.y):
                result = operation(self.matrix[i][j],  other.matrix[i][j])
                m.matrix[i][j] = result
        return m

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
        return self.element_wise(other, lambda a, b: a + b)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        return self - other

    def __sub__(self, other):
        return self.element_wise(other, lambda a, b: a - b)

#==============================================================================
class SquareMatrix(Matrix):

    def __init__(self, size, assignment=lambda a,b: 0):
        super(SquareMatrix, self).__init__(size, size, assignment)
        
#==============================================================================
class IdentityMatrix(SquareMatrix):

    def __init__(self, size):
        super(IdentityMatrix, self).__init__(size)
        for i in range(self.x):
            self[i][i] = 1

#==============================================================================
if (__name__ == "__main__"):
    m = Matrix(3, 4, lambda a,b: a+b)
    #m[0][0] = 1
    #m[0][1] = 1
    #m[2][2] = 1
    i = IdentityMatrix(3)

    #m.out()
    #m += i
    i += i
    print m
