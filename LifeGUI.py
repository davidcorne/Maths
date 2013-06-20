#!/usr/bin/env python
# Written by: DGC

# python imports
from Tkinter import *

# local imports

#==============================================================================
class LifeGUI(Toplevel):
    
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent

#==============================================================================
if (__name__ == "__main__"):
    top = Tk()
    view = LifeGUI(top)

    #calculator = Calculator()
    #presenter = Presenter(calculator, view)

    top.withdraw()
    top.mainloop()
