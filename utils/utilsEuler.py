#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

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


# Test if a number is prime by trial division
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i == 0):
            return False

    return True

# Test if a string is a palindromes
def isPalindrome(n):
    if (len(str(n))%2==0):
        return str(n)[:len(str(n))/2] == str(n)[len(str(n))-1:len(str(n))/2-1:-1]
    else:
        return str(n)[:len(str(n))/2] == str(n)[len(str(n))-1:len(str(n))/2:-1]

# Return the nth triangular number
def triangular(n):
    return n * (n + 1)/2
