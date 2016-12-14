#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

# terribly dumb version
# I would have generated all of the primes untils 9876543210 with eratosthenesList
# But python gives me an out of memory error.
# So we generates all the pandigitals, then we remove the muliples of the primes
# then we test the primness of the remaining and finally we get the largest one.
# That's a terrible version which **really** needs to be improved

def eliminatePrimesMultiple(pandigitals, primes):
    for x in pandigitals:
        for i in primes:
            if (x[0] % i == 0):
                x[1] = False
                break

    return [x[0] for x in pandigitals if x[1]]

def main():
    base="12345678900"

    pandigitals = []
    for i in range(0, len(base)):
        base = base[:-1]
        print "Generating pandigitals of " + base
        pandigitals += [int(x) for x in utilsEuler.permute(base)]

    pandigitals.sort()

    primes = utilsEuler.eratosthenesList(200)

    print "total of pandigitals: " + str(len(pandigitals))

    print "Removing multiples of primes: "
    for p in primes:
        pandigitals = [x for x in pandigitals if x % p != 0]
        print str(p) + "\tremaining: " + str(len(pandigitals))

    print "Removing non primes: "
    pandigitals = [x for x in pandigitals if utilsEuler.isPrime(x)]
    print "remaining: " + str(len(pandigitals))

    i = max(pandigitals)
    print "largest pandigitals prime: " + str(i)

main()
