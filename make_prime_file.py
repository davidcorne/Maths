#!/usr/bin/env python
# Written by: DGC
# Reads primes from file primes.txt into a list primes, 
# then works out more primes and appends them to primes.txt 
how_many_primes = 0
import fileinput
import time
import math
t_start = time.time()

limit = 100000001
#limit = input("Primes less than what number? (enter 0 or less for default of 100000001)\n")
if (limit <= 0):
    limit = 100000001
percent_change = 1
print("Limit used is"),
print(limit)
print("Percentage change used is"),
print(percent_change)
primes = []
i = 3

for line in fileinput.input("primes.txt"):
    temp_prime = int(float(line))
    if (temp_prime > limit):
        break
    primes.append(temp_prime)
    i = temp_prime
    how_many_primes += 1
percent_last = (float(i)/float(limit))*100
print("Files opened")
if (i > 3):
    print("Currently"),
    print(percent_last),
    print("% through, running for"),
    print(str(time.time()-t_start)),
    print("seconds")

with open("primes.txt","a") as file:
    if (not primes):
        primes.append(2)
        file.write(str(2))
        file.write("\n")        
        how_many_primes += 1
    file.read
    while (1):
        if i > limit:
            break
        truth = 1
        for j in primes:
            if (j > math.sqrt(i)):
                break
            if (i % j) == 0:
                truth = 0
                break
        if truth == 1:
            primes.append(i)
            how_many_primes += 1
        i += 1
        percent = (float(i)/float(limit))*100
        if percent - percent_last > percent_change:
            print("Currently"),
            print(percent),
            print("% through, running for"),
            print(str(time.time()-t_start)),
            print("seconds")
            percent_last = percent
    for p in primes:
        file.write(str(p))
        file.write("\n")
print("FINISHED!!!!!!")
print("Calculation time:"),
print(str(time.time()-t_start))
