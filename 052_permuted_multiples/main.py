#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

found = False
i = 0

# Test all the numbers
while not found:
    i += 1
    if (i % 1000000 == 0):
        print i

    # test if j * the number is a permutation of the number
    # if it's not we break the loop and test the next number
    for j in range(1, 7):
        s1 = str(i)
        s2 = str(j*i)
        if (not utilsEuler.isPermutation(s1, s2)):
            break

    # if j == 6 then the all the multiples are permutations
    # so the loop is over
    if j == 6:
        found = True
        s = ''
        for j in range(1, 7):
            s += str(i*j) + "  " 
        print "number: " + s
