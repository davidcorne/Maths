#!/usr/bin/env python
# Written by: DGC
# Inspired by this blog post:
# http://www.johndcook.com/blog/2012/10/02/sum-of-4th-powers/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+TheEndeavour+%28The+Endeavour%29
# python imports

# local imports

def find_smallest_sum():
    """ 
    Looks for the smallest number that is expressible as the sum of two fourth 
    powers in two different ways. e.g 653518657 = 158^4 + 59^4 = 134^4 + 133^4
    """
    # find all the pairs 
    pairs = find_pairs()
    powers = dict()
    for pair in pairs:
        result = (pair[0] ** 4) + (pair[1] ** 4)
        # found two
        if (result in powers.keys()):
            return (powers[result], pair)
        powers[result] = pair
    
def find_pairs():
    l = []
    # fourth root of 653518657 is 159.88749473445046
    for i in range(1,160):
        for j in range(1,i):
            l.append((i, j))
    return l

#==============================================================================
if (__name__ == "__main__"):
    pair = find_smallest_sum() 
    print(
        str(pair[0][0]) + 
        "^4 + " +
        str(pair[0][1]) +
        "^4 = " +
        str((pair[0][0] ** 4) + (pair[0][1] ** 4))
        )
    print(
        str(pair[1][0]) + 
        "^4 + " +
        str(pair[1][1]) +
        "^4 = " +
        str((pair[1][0] ** 4) + (pair[1][1] ** 4))
        )
