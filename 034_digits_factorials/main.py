#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This worked with some luck: To test the program I put a limit
# to 50000 and randomly tried the answer, it worked...
#
# Now I should improve it to make it stop on a smart limit

import math

maxFound = False
k = 3
i = k

numbers = []
while (not maxFound):
    i += 1

    facto = sum([ math.factorial(int(j)) for j in str(i)])

    if (facto == i):
        numbers.append(i)

    if (i >= k + 50000):
        maxFound = True

    print str(i) + "\t" + str(facto) + ("\tTrue" if facto <= i else "")

print numbers

print sum(numbers)
