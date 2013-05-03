#!/usr/bin/env python
# Written by: DGC
# Inspired from here
# http://www.johndcook.com/blog/2012/09/25/ramanujans-factorial-approximation/

# python imports
import math
# local imports

def ramanujan2(x):
    fact = math.sqrt(math.pi)*(x/math.e)**x
    fact *= (((8*x + 4)*x + 1)*x + 1/30.)**(1./6.)
    if (x - int(x) == 0):
        fact = int(fact)
    return fact

#==============================================================================
if (__name__ == "__main__"):
    print(ramanujan2(5))
    print(ramanujan2(5.0))
    print(ramanujan2(5.1))
