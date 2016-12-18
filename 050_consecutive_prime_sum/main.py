#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

# Incredibly long solution: the largest sequence is found pretty quickly
# but the program should stop much sooner.
# A new implementation should follow the solution here https://projecteuler.net/thread=50;page=9
# which is much more efficient

def main():

    limit = 1000000
    # limit = 1000
    primes = utilsEuler.eratosthenesList(limit)
    maxSequence = []

    for indexP in xrange(len(primes)-1):
        print str(indexP) + " / " + str(len(primes)-1)
        indexS = indexP
        sequence = [primes[indexP]]

        while (sum(sequence) < limit and indexS <= len(primes)):
            indexS += 1
            sequence.append(primes[indexS])
            # print "\t" + str(sequence)

            if (sum(sequence) in primes and (len(sequence) > len(maxSequence))):
                maxSequence = list(sequence)
                print "new max sequence: " + str(maxSequence) + "\tlenmax: " + str(len(maxSequence)) + "\tsum: " + str(sum(maxSequence))

    print "max sequence: " + str(maxSequence) + "\tlenmax: " + str(len(maxSequence)) + "\tsum: " + str(sum(maxSequence))

main()
