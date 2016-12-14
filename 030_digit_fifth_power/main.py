#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

# We search the maximum of digit that a number can have to
# still be able to fit the property.
def findLimit(power):
    found = False
    i = 0

    while (not found):
        i += 1
        s = ''.join([ '9' for _ in xrange(i)])
        n = int(s)

        if ( n > sum([pow(int(j), power) for j in s])):
            found = True

    return int(''.join(['9' for _ in xrange(i)]))


# Test if a number n is also the sum of the fifth power
# of its digits
def isSumOfPowerDigit(n, power):
    return n == sum([pow(int(i), power) for i in str(n)])

def main():
    # The power to apply to each digit
    # 4 allows to find 19316 as in the example
    # 5 allows to find ...... which is the result of the problem
    power = 5

    # We have to test a finite number of numbers
    # This function finds the limit for the researched power
    limit = findLimit(power)

    # For each number between 2 and the limit found before,
    # test if it has the property reasearched and add it to
    # the total result if it does
    result = 0
    for i in range(2, limit):
        if isSumOfPowerDigit(i, power):
            result += i
            print str(i) + "\t: sum :\t" + str(result)

    print "Result: " + str(result)

main()
