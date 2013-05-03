#!/usr/bin/env python
# Written by: DGC

class PascalTriangle(object):
    
    def __init__(self, n):
        self.n = n
        self.triangle = []
        self.calculate()

    def calculate(self):
        for i in range(self.n + 1):
            self.triangle.append([1])
            for j in range(1, i):
                number = self.triangle[i - 1][j - 1] + self.triangle[i - 1][j] 
                self.triangle[i].append(number)
            if (i != 0):
                self.triangle[i].append(1)

    def find_digits(self, number):
        ret_val = 0
        copy = number
        while (copy > 0):
            ret_val += 1
            copy = copy / 10
        return ret_val

    def print_number(self, number, spaces):
        digits = self.find_digits(number)
        assert digits <= spaces
        to_print = ""
        for i in range((spaces - digits) / 2):
            to_print += " "
        to_print += str(number)
        for i in range((spaces - digits) / 2):
            to_print += " "
        if ((spaces - digits) % 2 == 1):
            to_print = " " + to_print
        return to_print
        
    def out(self):
        largest = self.triangle[self.n][self.n / 2]
        print("largest: %i" %(largest))
        digits = self.find_digits(largest)
        # if the digits are even then make them odd
        if (digits % 2 == 0):
            digits += 1
        print("digits: %i" %(digits))
        to_print = "\n"
        for i in range(self.n, -1, -1):
            line = ""
            for j in range(self.n - i):
                line += "  "
            for j in range(0, i + 1):
                for k in range(digits + 1 - self.find_digits(self.triangle[i][j])):
                    line += " "
                line += str(self.triangle[i][j])
            to_print = "\n" + line + to_print
        print(to_print)

    def new_out(self):
        largest = self.triangle[self.n][self.n / 2]
        print("largest: %i" %(largest))
        digits = self.find_digits(largest)
        # if the digits are even then make them odd
        if (digits % 2 == 0):
            digits += 1
        print("digits: %i" %(digits))
        #start = len(self.triangle[])

#==============================================================================
if (__name__ == "__main__"):
    tri = PascalTriangle(15)
    tri.out()
    print("")
    tri.new_out()

#  |-||-||-||-||-||-||-||-||-||-||-||-||0||-||-||-||-||-||-||-||-||-||-||-||-|
#  |-||-||-||-||-||-||-||-||-||-||-||0||-||0||-||-||-||-||-||-||-||-||-||-||-|
#  |-||-||-||-||-||-||-||-||-||-||0||-||0||-||0||-||-||-||-||-||-||-||-||-||-|
#  |-||-||-||-||-||-||-||-||-||0||-||0||-||0||-||0||-||-||-||-||-||-||-||-||-|
#  |-||-||-||-||-||-||-||-||0||-||0||-||0||-||0||-||0||-||-||-||-||-||-||-||-|
#  |-||-||-||-||-||-||-||0||-||0||-||0||-||0||-||0||-||0||-||-||-||-||-||-||-|
#  |-||-||-||-||-||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||-||-||-||-||-|
#  |-||-||-||-||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||-||-||-||-|
#  |-||-||-||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||-||-||-|
#  |-||-||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||-||-|
#  |-||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||-|
#  |-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-|
#  |0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0||-||0|

