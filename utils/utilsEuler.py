#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,
# 73,79,83,89,97,101,103, 107,109,113,127,131,137,139,149,
# 151,157,163,167,173,179,181,191,193,197,199,211,223,227,
# 229,233,239,241,251,257,263,269,271,277,281,283,293,307,
# 311,313,317,331,337,347, 349,353,359,367,373,379,383,389,
# 397,401,409,419,421,431,433,439,443,449,457,461,463,467,
# 479,487,491,499,503,509,521,523,541

# Create a generator for the primes numbers under limit
# The generator can be used only once
def eratosthenesGenerator(limit):
    # Generating the list and marking 0 and 1
    A = [True for i in range(limit)]
    A[0] = A[1] = False

    # Using yield to create a generator containing the prime numbers
    for (i, isprime) in enumerate(A):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                A[n] = False

# Returs a list of the primes numbers under limit
def eratosthenesList(limit):
    return [i for i in eratosthenesGenerator(limit)]

# Test if a string is a palindromes
def isPal(n):
    if (len(str(n))%2==0):
        return str(n)[:len(str(n))/2] == str(n)[len(str(n))-1:len(str(n))/2-1:-1]
    else:
        return str(n)[:len(str(n))/2] == str(n)[len(str(n))-1:len(str(n))/2:-1]
