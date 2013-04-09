#!/usr/bin/env python
# Written by: DGC

#==============================================================================
class Fractal(object):

    def __init__(self, iterations, distance):
        """ 
        Sets up how many iterations to do and the distance from the origin to 
        limit by.
        """
        self.iterations = iterations
        self.distance = distance
        self.colours = []
        for i in range(self.iterations):
                colour = int(255 * (self.iterations - i))
                self.colours.append("#%02d%02d%02d" % (colour, colour, colour))

    def calculate(self, c):
        """ 
        Checks if c is whithin distance after iterations applications of the 
        Mandelbrot algorithm; z = z^2 + c. 
        """
        # normally start from z = 0 but then the first iteration is c anyway.
        z = c
        for i in range(1, self.iterations):
            z = self.algorithm(z, c)
            if (abs(z) > self.distance):
                return self.colours[i]
        return "black"

    def algorithm(self, *args):
        raise NotImplementedError

class Mandelbrot(Fractal):

    def __init__(self, iterations, distance):
        super(Mandelbrot, self).__init__(iterations, distance)

    def algorithm(self, z, c):
        return z*z + c

class DGC(Fractal):

    def __init__(self, iterations, distance):
        super(DGC, self).__init__(iterations, distance)

    def algorithm(self, z, c):
        return z*z*z*z + c

#==============================================================================
if (__name__ == "__main__"):
    pass
