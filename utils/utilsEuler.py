#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import re

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

# Same as eratosthenesGenerator but use a while loop instead of a for loop
# This way the function can generate sieve with much more number without
# memory error
def eratosthenesGenerator2(limit):
    # Generating the list and marking 0 and 1
    A = [True for i in range(limit)]
    A[0] = A[1] = False

    # Using yield to create a generator containing the prime numbers
    for (i, isprime) in enumerate(A):
        if isprime:
            yield i
            n = i*i - i
            while (n<limit-i):
            # for n in xrange(i*i, limit, i):     # Mark factors non-prime
                n += i
                A[n] = False

# Returs a list of the primes numbers under limit
def eratosthenesList(limit):
    # return [i for i in eratosthenesGenerator(limit)]
    return [i for i in eratosthenesGenerator2(limit)]


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

# Recursively find permutations of a string
def permute(n):
    if (len(n) == 2):
        return [str(n), str(n[1]+n[0])]
    else:
        list = []
        for i in n:
            sub = permute(re.sub(i, '', n))

            for s in sub:
                list.append(i + s)
                if (len(list) % 1000000 == 0):
                    print "+1000000 permutations: " + i+s

        return list

# Solves an equation of the form ax^2 + bx + c = 0
# Returns only real solutions (delta >= 0) in a list
def solveSecondDegreeEquation(a, b, c):
    d = (b*b) - (4*a*c)

    if (d > 0):
        return [(-1*b-math.sqrt(d))/(2*a), (-1*b+math.sqrt(d))/(2*a)]
    elif (d == 0):
        return (-1*b)/(2*a)
    else:
        return None

# Generate the Nth pentagonal number
def getPentagonal(n):
    return n * (3*n - 1) * 0.5

# Check if a number is pentagonal
def isPentagonal(x):
    solutions = solveSecondDegreeEquation(3, -1, -2 * x)

    for s in solutions:
        if (s.is_integer() and s > 0):
            return True

    return False

# Defines if the string s2 is a permutation of the string s1
def isPermutation(s1, s2):
    if (len(s1) == len(s2)):
        return (sorted(s1) == sorted(s2))
    return False
