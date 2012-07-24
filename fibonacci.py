#!/usr/bin/env python
# Written by: DGC
# finds the first n fibonacci numbers

def fibonacci_less(n):
    # returns all fibonacci numbers less than n
    fibon = [1,1]
    num = 1 #the length of the list
    while (fibon[num] < n):
        fibon.append(fibon[num] + fibon[num-1])
        num +=1
    return fibon[0:num]

def fibonacci_num(n):
    # returns a list of the first n fibonacci number
    fibon = [1,1]
    num = 1 #the length of the list
    while (num < n):
        fibon.append(fibon[num] + fibon[num-1])
        num +=1
    return fibon[0:num]
    
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
    
fibon = fibonacci_num(200000)
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

