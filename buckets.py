#!/usr/bin/env python
# Written by: DGC

# Taken from the following blog entry:
# http://www.johndcook.com/blog/2012/10/05/n-buckets-n-balls/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+TheEndeavour+%28The+Endeavour%29

# Suppose you have a large number of buckets and an equal number of balls. You 
# randomly pick a bucket to put each ball in one at a time. When you're done, 
# about how what proportion of buckets will be empty?
# 
# One line of reasoning says that since you have as many balls as buckets, each
#  bucket gets one ball on average, so nearly all the buckets get a ball.
# 
# Another line of reasoning says that randomness is clumpier than you think. 
# Some buckets will have several balls. Maybe most of the balls will end up 
# buckets with more than one ball, and so nearly all the buckets will be empty.
# 
# Is either extreme correct or is the answer in the middle? Does the answer 
# depend on the number n of buckets and balls? (If you look at the cases n = 1
#  and 2, obviously the answer depends on n. But how much does it depend on n 
# if n is large?) Hint: There is a fairly simple solution.

# python imports

import random

def main(n):
    """ 
    n is the number of buckets, runs the code 1000 times, averages the result
    and returns it as a %.
    """
    tries = 1000
    results = []
    for index in range(tries):
        buckets = []
        for i in range(n):
            buckets.append([])
        # randomly place the balls
        for i in range(n):
            random.choice(buckets).append(i)
        empty = 0
        for bucket in buckets:
            # it is empty
            if (not bucket):
                empty += 1
        results.append((empty / float(n)))
    return (100 * (sum(results) / float(tries)))


#==============================================================================
if (__name__ == "__main__"):
    for i in (10, 100, 1000, 10000, 100000):
        print(str(i) + ": " + str(main(i)) + "%")
