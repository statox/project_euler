#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler



# IMPORTANT IMPROVED VERSION OF eratosthenesGenerator
# IT CAN NOW HANDLE A LARGER LIMIT EVEN IN PYTHON 2

# Incredibly long solution: the largest sequence is found pretty quickly
# but the program should stop much sooner.
# A new implementation should follow the solution here https://projecteuler.net/thread=50;page=9
# which is much more efficient

# # Create a generator for the primes numbers under limit
# # The generator can be used only once
# def eratosthenesGenerator(limit):
#     # Generating the list and marking 0 and 1
#     A = [True for i in range(limit)]
#     A[0] = A[1] = False
# 
#     # Using yield to create a generator containing the prime numbers
#     for (i, isprime) in enumerate(A):
#         if isprime:
#             yield i
#             for n in xrange(i*i, limit, i):     # Mark factors non-prime
#                 A[n] = False
# 
# def eratosthenesGenerator2(limit):
#     # Generating the list and marking 0 and 1
#     A = [True for i in range(limit)]
#     A[0] = A[1] = False
# 
#     # Using yield to create a generator containing the prime numbers
#     for (i, isprime) in enumerate(A):
#         if isprime:
#             yield i
#             n = i*i - i
#             while (n<limit-i):
#             # for n in xrange(i*i, limit, i):     # Mark factors non-prime
#                 n += i
#                 A[n] = False
# 
# # Returns a list of the primes numbers under limit
# def eratosthenesList(limit):
#     return [i for i in eratosthenesGenerator2(limit)]

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
