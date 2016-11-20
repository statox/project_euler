#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Return a list of prime numbers until limit
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

# Return a list of prime factors for a natural n
def trialDivision(n):
    if n < 2:
        return []

    primeFactors = []
    for p in eratosthenes(int(pow(n, 0.5))):
        if (p*p > n):
            break
        while (n%p == 0):
            primeFactors.append(p)
            n //= p

    if (n > 1):
        primeFactors.append(n)

    return primeFactors

print trialDivision(13195)
print trialDivision(600851475143)
