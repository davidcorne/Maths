#!/usr/bin/env python
# Written by: DGC
# working out things with the harmonic series.

import time

#==============================================================================
if (__name__ == "__main__"):
    time_start = time.time()
    sum = 0
    num = 1
    last_sum = 0.1
    while (sum < 50):
        sum += 1/float(num)
        num += 1
        if (sum > last_sum + 0.1):
            print(
                "Sum: " + 
                str(sum) +
                " Time: " +
                str(time.time() - time_start) +
                " Iterations: " + 
                str(num)
                )
            last_sum += 0.1
    print(num)
