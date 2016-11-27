#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

# Test if a number is prime by trial division
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i == 0):
            return False

    return True

# Return the number of consecutive primes given by the
# quadratic expression n*n + a*n + b
def consecutivePrimes(a, b):
    n=1
    while (n*n + a*n + b >=0 and isPrime(n*n + a*n + b)):
        n+=1

    return n

# Search the number of consecutive primes for each coefficents a and b
def search():
    saveA=-1000
    saveB=-1000
    maxPrimes=0

    for a in range(-1001, 1001):
        # print a
        # for b in range(-1001, 1001):
        for b in range(-1001, 1001):
            n = consecutivePrimes(a, b)

            if (n > maxPrimes):
                saveA = a
                saveB = b
                maxPrimes = n

                # print "a: " + str(a) + "\tb: " + str(b) + "\tn" + str(n) + "\t prod: " + str(a*b)


    print "Coefficients giving the max number of primes"
    print "a: " + str(saveA) + "\tb: " + str(saveB) + "\tproduct: " + str(saveA*saveB)

def main():
    search()

main()
