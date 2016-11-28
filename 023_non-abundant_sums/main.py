#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This version is to be improved:
# I get the right result but for an execution time of about 45mn
# Found first number which can't be written as the sum of 2 abundant numbers:
# 20161
# Sum to find:
# 4179871

import math

# Global variable containing the abundant numbers
a = []

# Return a list of divisors for a natural n
def trialDivision(n):
    factors = []
    i = 1
    factors.append(1)

    while (i <= math.sqrt(n)):
        i+=1
        if (n % i == 0):
            factors.append(i)
            factors.append(n / i)

    # append(n/i) creates duplicates so we 
    # remove them with set()
    return set(factors)

# Test if a number is abundant
def isAbundant(n):
    if (n == 2):
        return False
    divisors = trialDivision(n)
    if (sum(divisors) > n):
        return True
    else:
        return False

# Generate abundant numbers lower than a limit
def generateAbundants(limit):
    abundants = []
    for i in range(12, limit+1):
        if (isAbundant(i)):
            abundants.append(i)

    return abundants

# Generate the numbers lower than limit which can be
# written as a sum of abundant
def sumsOfAbundants(limit):
    abundant = generateAbundants(limit)
    s = []
    i = j = 0
    for i in range (0, len(abundants)):
        for j in range (0, len(abundants)):
            tmpSum = abundant[i] + abundant[j]
            if (tmpSum > limit):
                break
            s.append(tmpSum)

    s = list(set(s))
    s.sort

    return s

# Test if a number can be written as the sum of 2 abundant numbers
def isSumOf2Abundant(i):
    n = -1
    m = 0
    isSum = False

    while (n < len(a)-1):
        n += 1
        m = 0
        while (a[n] + a[m] <= i and m <len(a)-1 ):
            m += 1
            # print "a[" + str(n) + "]: " + str(a[n]) + "\ta[" + str(m) + "]: " + str(a[m]) + "\t= " + str(a[n]+a[m]) 

            if (a[n] + a[m] == i):
                # print str(i) + " = " + str(a[n]) + " + " + str(a[m])
                return True

    return False

def main():
    global a

    limit = 28123

    print "Generating abundant numbers lower than " + str(limit)
    a = list(set(generateAbundants(limit)))
    print str(len(a)) + " abundant numbers generated"

    print "Searching for greatest number which can not be expressed as sum of abundant numbers"

    toSum = []
    for i in range(28130, 24, -1):
        if (not isSumOf2Abundant(i)):
            print str(i) + " is not sum of abundants"
            toSum.append(i)

    for i in range (1, 24):
        toSum.append(i)

    print "list: " + str(toSum)
    print "sum: " + str(sum(toSum))
    return

main()
