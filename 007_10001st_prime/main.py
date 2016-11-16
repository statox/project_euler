#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import timeit

def eratosthenes(limit):
    #print "Generating numbers"
    A = [True for i in range(limit)]

    #print "Applying sieve"
    for i in range(2, int(math.sqrt(len(A)))):
        if (A[i]):
            j=i
            while (j<len(A)-i):
                j+=i
                A[j]=False

    #print "Getting primes numbers"
    primes=[]
    for i in range(2, len(A)):
        if (A[i]):
            primes.append(i)

    return primes

def sundaram(limit):
    iterations=0
    n = int((limit/2))
    #print "Generating numbers"
    A = [i for i in range(n)]

    #print "Applying sieve"
    i=0
    while (i < n):
        i+=1
        j=i-1
        k=i+j+(2*i*j)

        while (k < n):
            j+=1
            iterations += 1
            k = i + j + (2*i*j)

            if (k < n):
                A[k] = -1

    #print "Getting primes numbers"
    primes = [2]
    for i in A[1:]:
        if (i != -1):
            i = 2*i + 1
            primes.append(i)

    return primes

# Translation from here: http://www.geeksforgeeks.org/sieve-of-atkin/
def atkin2(limit):
    sieve = [ False for i in range(limit)]

    for x in range(1, int(math.sqrt(limit))+1):
        for y in range(1, int(math.sqrt(limit))+1):

            n = (4*x*x)+(y*y)
            if (n <= limit and (n%12 == 1 or n%12 == 5)):
                sieve[n] = True

            n = (3*x*x)+(y*y)
            if (n <= limit and n % 12 == 7):
                sieve[n] = True
 
            n = (3*x*x)-(y*y);
            if (x > y and n <= limit and n % 12 == 11):
                sieve[n] = True

    for r in range(5, int(math.sqrt(limit))+1):
        if (sieve[r]):
            for i in range(r*r, limit, r*r):
                sieve[i] = False

    primes = [2, 3]
    for i in range(5, limit):
        if (sieve[i]):
            primes.append(i)

    return primes


# Based on the algorithm given here: https://en.wikipedia.org/wiki/Wheel_factorization
# I thought that I would use it in atkin but it turns out that I'm not
def wheelFactorization(firstPrimes, limit):
    # 1. Get first primes
    #print "1. First primes: " + str(firstPrimes)

    # 2. Find circumference
    #print "2. Wheel circumference: "
    n = reduce(lambda x, y: x*y, firstPrimes)
    #print n

    # 3. Create inner-most circle
    #print "3. Inner-most circle: "
    wheel = [i for i in range(1, n+1)]
    #print wheel

    # 4. Strike off multiples of base primes
    #print "4. Strike multiples of primes: "
    stepFourStokes = []
    for i in firstPrimes:
        j=1
        while (i*j < n):
            j += 1
            if (wheel[(i*j)-1] > -1):
                stepFourStokes.append(wheel[(i*j)-1])
            wheel[(i*j)-1] = -1

    #print str(wheel)

    # 5-6. Add more rings
    #print "5-6. Add more rings: "
    [wheel.append(i) for i in range(n+1, limit)]
    #print str(wheel)

    # 7. Strike off 1
    #wheel[0] = -1
    ##print "7. Strike off 1" 

    # 8. Strike off spokes of the first primes
    #print "8. Strike off spokes of primes"
    for p in firstPrimes:
        i = n
        while ((p+i)-1<len(wheel)):
            wheel[(p+i)-1] = -1
            i += n

    #print str(wheel)

    # 9. Strike off multiples of primes struck in step 4
    #print "9. Strike off the spokes of multiples of prime stroke in step 4"
    for m in stepFourStokes:
        #print "\tspoke of " + str(m)
        i = n
        while ((m+i)-1<len(wheel)):
            wheel[(m+i)-1] = -1
            i += n

    #print str(wheel)

    # 10. Get the remaining numbers
    #print "10. Remaining numbers: "
    remaining = [ i for i in wheel if i > -1 ]

    #print str(remaining)

    return remaining

def timeFunctions():
    limit = 10000000
    t = timeit.Timer("eratosthenes(" + str(limit) + ")", "from __main__ import eratosthenes")
    time = t.timeit(1)
    print "took %fs\n" % (time,)    

    t = timeit.Timer("sundaram(" + str(limit) + ")", "from __main__ import sundaram")
    time = t.timeit(1)
    print "took %fs\n" % (time,)    

    t = timeit.Timer("atkin2(" + str(limit) + ")", "from __main__ import atkin2")
    time = t.timeit(1)
    print "took %fs\n" % (time,)    

def find10001stPrime():
    limit=150000
    print '====== Eratosthenes ======'
    primes = eratosthenes(limit)

    if (len(primes) > 10003):
        print "10001st: " + str(primes[10000])
    else:
        print "not enough primes: " + str(len(primes))

    print '====== Sundaram ======'
    primes = sundaram(limit)
    if (len(primes) > 10003):
        print "10001st: " + str(primes[10000])
    else:
        print "not enough primes: " + str(len(primes))

    print '====== Atkin ======'
    primes = atkin2(limit)
    if (len(primes) > 10003):
        print "10001st: " + str(primes[10000])
    else:
        print "not enough primes: " + str(len(primes))

def showFound():
    limit=150
    print '====== Eratosthenes ======'
    primes = eratosthenes(limit)

    print primes

    print '====== Sundaram ======'
    primes = sundaram(limit)
    print primes

    print '====== Atkin ======'
    primes = atkin2(limit)
    print primes



def main():
    # timeFunctions()
    find10001stPrime()
    # showFound()

main()

