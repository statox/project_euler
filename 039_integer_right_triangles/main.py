#!/usr/bin/env python
# -*- coding: utf-8 -*-

# First version: it works but it is just a brute force method
# A better method can surely be found
import math

perimeters = {}

maxPerimeter = 0
maxComb = 0

for p in range(1, 1001):

    comb = 0
    for a in range(1, p):
        for b in range(1, a):
            if (a + b + math.sqrt(a*a + b*b) == p):
                comb += 1
            # Don't test combinations which give a perimeter > p
            # Reduce the number of iterations from 165668499 to 25684990
            elif (a + b + math.sqrt(a*a + b*b) > p):
                break

    if (comb > maxComb):
        maxComb = comb
        maxPerimeter = p

    print str(p) + "\t" + (str(comb) if comb > 0 else "")

print "maxPerimeter: " + str(maxPerimeter)
print "maxComb: " + str(maxComb)
