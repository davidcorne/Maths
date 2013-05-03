#!/usr/bin/env python
# Written by: DGC
# finds the first n fibonacci numbers

import math

#==============================================================================
def fibonacci_generator(limit=10000000):
    i = 0
    j = 1
    while (True):
        if (i > limit):
            break
        yield i
        i, j = j, i+j

#==============================================================================
def fibonacci_less(n):
    # returns all fibonacci numbers less than n
    fibon = [1,1]
    num = 1 #the length of the list
    while (fibon[num] < n):
        fibon.append(fibon[num] + fibon[num-1])
        num +=1
    return fibon[0:num]

#==============================================================================
def fibonacci_num(n):
    # returns a list of the first n fibonacci number
    fibon = [1,1]
    while (len(fibob) <= n):
        fibon.append(fibon[num] + fibon[num-1])
    return fibon
    
#==============================================================================
def exact_fibonacci(n):
    """ Returns the nth fibonacci number using the exact formula. """
    Phi = ((1 + math.sqrt(5)) / 2.0)
    phi = ((1 - math.sqrt(5)) / 2.0)
    return (((Phi ** n) - (phi ** n)) / math.sqrt(5))

#==============================================================================
def fibonacci_num_big(n):
    # returns the nth fibonacci number, works for big number as none stored
    f_1 = 1
    f_2 = 1
    num = 1 #the length of the list
    while (num < n):
        tmp = f_1 + f_2
        f_1 = f_2
        f_2 = tmp
        num +=1
    return f_2
    
#==============================================================================
def main():
    fibon = fibonacci_num(200)
    num = 0
    broke = 0
    for fib in fibon:
        if (broke > 20):
            break
        if (fib != fibonacci_num_big(num)):
            print(num),
            print(fib),
            print(fibonacci_num_big(num))
            print(fib - fibonacci_num_big(num)) 
            broke += 1
        num += 1

#fibonacci = fibonacci_num_big(1000000)
#print(fibonacci)
#print("\nnumber of digits:")
#print(len(str(fibonacci)))


#==============================================================================
if (__name__ == "__main__"):
    gen = fibonacci_generator()
    for i in gen:
        print i
