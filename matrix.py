#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class Matrix(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.matrix = []
        for j in range(self.y):
            row = []
            for i in range(self.x):
                row.append(0)
            self.matrix.append(row)

    def out(self):
        for j in range(self.y):
            for i in range(self.x):
                print(self.matrix[j][i]),
            print("")
                    
    def __getitem__(self, key):
        # returns the keyth column so that element (x, y) is accessed 
        # as follows: Matrix[x][y]
        column = []
        for i in range(self.y):
            column.append(self.matrix[i][key])
        return column

    def __setitem__ (self, key, value):
        # 
        print("SETTING ITEM")


#==============================================================================
class SquareMatrix(Matrix):

    def __init__(self, size):
        super(SquareMatrix, self).__init__(size, size)
        
def test(value, message):
    """ This asserts against the value printing for either pass or fail. """
    assert value, message
    print("PASSED: %s" %(message))
    print("")

#==============================================================================
if (__name__ == "__main__"):
    m = Matrix(5, 3)
    m[3] = 17
    print(m[3][0])
    m.out()
