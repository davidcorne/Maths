#!/usr/bin/env python
# Written by: DGC

# python imports

# local imports

#==============================================================================
class Mandelbrot(object):
    
    def __init__(self, size, iterations = 20, distance = 2):
        """ 
        Sets up how many iterations to do and the distance from the origin to 
        limit by.
        """
        self.iterations = iterations
        self.distance = distance
        self.size = size
        self.colours = []
        # make a size x size grid.
        self.grid = [[0] * self.size for x in xrange(self.size)]
        
    def calculate(self, c):
        """ 
        Checks if c is whithin distance after iterations applications of the 
        Mandelbrot algorithm; z = z^2 + c. 
        """
        # normally start from z = 0 but then the first iteration is c anyway.
        z = c
        for index in range(1, self.iterations):
            z = z*z + c
            if (abs(z) > self.distance):
                return index
        return 0

#==============================================================================
if (__name__ == "__main__"):
    m = Mandelbrot(9)
