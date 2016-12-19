#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

def main():
    n = 2
    nbOfPrimes = 3

    # incrementing the size of the spiral while the ratio is > 10%
    while (nbOfPrimes/float(4*(n-1) + 1) > 0.1):
        n += 1

        # Calculate the new number on each diagonal
        newNumbers = ( 4*n*n - 10*n + 7, 4*n*n - 8*n  + 5, 4*n*n - 6*n  + 3, 4*n*n - 4*n  + 1)

        # Get the number of primes and add it to the previous count
        nbOfPrimes += sum([1 for x in newNumbers if utilsEuler.isPrime(x)])

        if (n % 1000 == 0):
            print "n: " + str(n)

    print "Final length: " + str(1 + 2 * (n-1)) + "\t for n: " + str(n)


main()
