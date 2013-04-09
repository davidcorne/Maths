#!/usr/bin/env python
# Written by: DGC
# A 'Dave' sequence is one which starts with two numbers a, b then the rule to
# continue is the next number is |a - b| etc.
# eg 7, 9, 2, 7, 5, 2, 3, 1, 2, 1, 1, 0, 1, 1, 0 ...
# this repeats when it reaches 0

def sequence(a, b):
    " prints how many numbers it takes to get to 0"
    seq = [a, b]
    while(seq[-1] != 0):
        seq.append(abs(seq[-1] - seq[-2]))
    return len(seq)

for i in range(100):
    for j in range(100):
        print("(%i, %i): %i" %(i, j, sequence(i,j)))
