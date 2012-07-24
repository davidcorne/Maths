#!/usr/bin/env python
# Written by: DGC
# working out things with the harmonic series.

import time

t_s = time.time()
sum = 0
num = 1
last_sum = 0.1
while (sum < 50):
    sum += 1/float(num)
    num += 1
    if (sum > last_sum + 0.1):
        print("Sum:"),
        print(sum),
        print("Time:"),
        print(str(time.time()-t_s)),
        print("Iterations:"),
        print(num)
        last_sum += 0.1
print(num)
