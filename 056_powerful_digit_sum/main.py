#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

# Return the sum of the digits of a number
def digitalSum(n):
    return sum([ int(x) for x in str(n)])

def main():
    maxSum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            currentSum=digitalSum(pow(a, b))

            if (currentSum > maxSum):
                maxSum = currentSum

    print 'max sum ' + str(maxSum)


main()
