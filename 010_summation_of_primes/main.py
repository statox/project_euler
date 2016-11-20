#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def eratosthenes(limit):
    # Generating the list and marking 0 and 1
    A = [True for i in range(limit)]
    A[0] = A[1] = False

    # Using yield to create a generator containing the prime numbers
    for (i, isprime) in enumerate(A):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                A[n] = False


def main():
    primes = eratosthenes(2000000)
    res = sum(primes)

    print res

main()
