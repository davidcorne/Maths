#!/usr/bin/env python
# Written by: DGC

import Benchmark

@Benchmark.benchmark
def recursive_factorial(n):
    return __recursive_factorial(n)

def __recursive_factorial(n):
    if (n == 1):
        return 1
    return n * __recursive_factorial(n - 1)

@Benchmark.benchmark
def inductive_factorial(n):
    ret_val = 1
    for i in range(2, n + 1):
        ret_val *= i
    return ret_val

#==============================================================================
if (__name__ == "__main__"):
    inductive_factorial(500)
    recursive_factorial(500)
    
