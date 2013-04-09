#!/usr/bin/env python
# Written by: DGC

# python imports
from Tkinter import *

# local imports

#==============================================================================
class Calculator(object):
    
    def __init__(self):
        self.total = 0

    def start(self, value):
        self.total = value

    def add(self, value):
        print(str(self.total) + " + " + str(value))
        self.total += value
        print("total is: " + str(self.total))

    def subtract(self, value):
        print(str(self.total) + " - " + str(value))
        self.total -= value
        print("total is: " + str(self.total))

    def multiply(self, value):
        print(str(self.total) + " * " + str(value))
        self.total *= value
        print("total is: " + str(self.total))

#==============================================================================
class Presenter(object):
    
    # pass in the view so it can be mocked
    def __init__(self, calculator, view):
        self.calculator = calculator
        
        self.view = view
        self.view.callback = self.symbol_added

    def symbol_added(self, symbol):
        print(symbol)
        if symbol in ["+", "-", "*", "="]:
            pass

#==============================================================================
class View(Toplevel):
    
    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        # hook up the delete button so that it quits the window and doesn't 
        # make the main program hang
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.title("Calculator")

        self.callback = None
        
        self.make_results_window()
        self.make_output_line()
        self.make_buttons()

    def make_results_window(self):
        self.results = StringVar()
        output = Entry(
            self,
            state="readonly",
            textvariable=self.results,
            justify="right"
            )
        output.grid(row=0, column=0, columnspan=4)

    def make_output_line(self):
        self.output = StringVar()
        output = Entry(
            self,
            state="readonly",
            textvariable=self.output,
            justify="right"
            )
        output.grid(row=1, column=0, columnspan=4)

    def make_buttons(self):
        button_list = [
            "7", "8", "9", "*", 
            "4", "5", "6", "-", 
            "1", "2", "3", "+"
            ]
        row_index = 2
        column_index = 0
        for label in button_list:
            cmd = lambda current_label=label: self.button_press(current_label)
            button = Button(self, text=label, command=cmd, height=2, width=4)
            button.grid(row=row_index, column=column_index)

            # now adjust the grid numbers
            column_index += 1
            if (column_index > 3):
                # time to go to a new row
                row_index += 1
                column_index = 0
        equals = Button(
            self, 
            text="=", 
            command=lambda : self.button_press("="), 
            height=2,
            width=8
            )
        equals.grid(row=6, column=2, columnspan=2)

    def button_press(self, button_label):
        self.callback(button_label)

#==============================================================================
class Calculator2(object):

    def calculate(self, input):
        return eval(input)

#==============================================================================
class Presenter2(object):
    
    # pass in the view so it can be mocked
    def __init__(self, calculator, view):
        self.calculator = calculator
        
        self.view = view
        self.view.callback = self.symbol_added
        
        self.numbers = ""

    def symbol_added(self, symbol):
        if symbol in ["+", "-", "*", "="]:
            self.evaluate(symbol)
        else:
            self.numbers += symbol
            self.view.output.set(self.view.output.get() + symbol)
            
    def evaluate(self, symbol):
        if (symbol == "="):
            result = self.calculator.calculate(self.numbers)
            self.view.results.set(str(result))
            self.numbers = ""
        else:
            self.numbers += " " + symbol + " "
            self.view.results.set(self.numbers)
        self.view.output.set("")

#==============================================================================
if (__name__ == "__main__"):
    top = Tk()
    view = View(top)

    #calculator = Calculator2()
    #presenter = Presenter2(calculator, view)

    calculator = Calculator()
    presenter = Presenter(calculator, view)

    top.withdraw()
    top.mainloop()
