#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# Return a list of divisors for a natural n
def trialDivision(n):
    factors = []
    i = 0

    while (i <= math.sqrt(n)):
        i+=1
        if (n % i == 0):
            factors.append(i)
            factors.append(n / i)

    # append(n/i) creates duplicates so we 
    # remove them with set()
    return set(factors)

# Return the nth triangular number
def triangular(n):
    return n * (n + 1)/2

# Search for the triangular with 500+ divisors
def main():
    i = 1
    n = triangular(i)

    while (len(trialDivision(n)) < 500):
        i += 1
        n = triangular(i)

    print str(n) + " has " + str(len(trialDivision(n))) + " divisors" 

main()
