#!/usr/bin/env python
# Written by: DGC

import Mandelbrot
import Fractal
from Tkinter import *
import time

#==============================================================================
class Gui(object):
    
    def __init__(self, size):
        self.parent = Tk()
        # we want a square grid
        # size need to be divisible by 8 
        self.size = size
        self.window = Canvas(
            self.parent,
            width = self.size,
            height = self.size
            )
        self.parent.title("Mandelbrot")
        self.window.pack()

        iterations = 20
        self.fractal = Fractal.Mandelbrot(iterations, 2)
        #self.fractal = Fractal.DGC(iterations, 2)
        self.calculate()
        self.make_grid()

        self.parent.mainloop()   
        
    def calculate(self):
        print("Calculation Started. Iterations: " + str(self.fractal.iterations))
        t = time.time()
        divisor = (self.size / 4.0)
        for x in range(self.size):
            real = x / divisor - 2
            for y in range(0, self.size):
                img = y / divisor - 2
                c = complex(real, img)
                # set the coordinate to the returned colour
                self.window.create_line(
                    x,
                    self.size - y,
                    x + 1,
                    self.size + 1 - y,
                    fill = self.fractal.calculate(c)
                    )
                self.window.pack()
        t = time.time() - t
        print("Calculation Complete!")
        print("Took: " + str(t) + " seconds")
        
    def make_grid(self):
        """ Divide the canvas into a 8 x 8 grid. """
        length = self.size / 8
        # draw horizontal lines
        for y in range(0, self.size, length):
            self.window.create_line(0, y, self.size, y, fill = "blue")
        
        # draw vertical lines
        for x in range(0, self.size, length):
            self.window.create_line(x, 0, x, self.size, fill = "blue")

        # draw the axes red
        self.window.create_line(
            0,
            self.size / 2,
            self.size, 
            self.size / 2, 
            fill = "red"
            )
        self.window.create_line(
            self.size / 2, 0,
            self.size / 2, 
            self.size, 
            fill = "red"
            )
        print("Grid Made.")


#==============================================================================
if (__name__ == "__main__"):
    pass
