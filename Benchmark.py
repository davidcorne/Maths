#!/usr/bin/env python
# Written by: DGC

# python imports

# local imports
import time

#==============================================================================
def benchmark(function):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    def wrapper(*args, **kwargs):
        t_start = time.clock()
        result = function(*args, **kwargs)
        t_end = time.clock() - t_start
        arg_string = ""
        for arg in args:
            arg_string += str(arg) + ", "
        for key in kwargs:
            arg_string += str(key) + " = " + str(kwargs[key]) + ", "
        arg_string = arg_string[0:-2]
        print(
            "Function: " +
            function.__name__ + 
            "(" +
            arg_string +
            ") executed in " +
            str(t_end) + 
            " seconds."
            )
        return result
    return wrapper
