#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Solves problem 32, pretty fast
#
# Note:
# 1 * 1000 = 1000 => 9 digits
# 10 * 100 = 1000 => 9 digits
# No other multications can give 9 digits
# Thus we only need to test numbers in this range

import re

def isPandigitalMultiplication(i, j):
    operation = str(i)+str(j)+str(i*j)

    # don't test strings with a 0 or less than 9 digits
    if ('0' not in operation and len(operation) == 9):
        # Remove duplicates to see if this is a pandigital operation
        noDuplicate = "".join(set(operation))

        if (len(noDuplicate) == 9):
            return i*j

    return None

def main():
    count = 0

    pandigitals = []

    for i in range(1,10):
        for j in range(1000, 10000):
            res = isPandigitalMultiplication(i, j)
            if (not res is None and not res in pandigitals):
                pandigitals.append(res)

    for i in range(10, 100):
        for j in range(100, 1000):
            res = isPandigitalMultiplication(i, j)
            if (not res is None and not res in pandigitals):
                pandigitals.append(res)

    print "pandigitals: " + str(pandigitals)
    print "sum: " + str(sum(pandigitals))

main()
