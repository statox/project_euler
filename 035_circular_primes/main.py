#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Probably can do faster... but it works

import utilsEuler

primes = utilsEuler.eratosthenesList(1000000)

res = []
while (len(primes) > 0):
    si = str(primes[0])

    # Directly add primes composed of one same numeber:
    if (si == len(si) * si[0]):
        res.append(si)
        primes.remove(int(si))
        print res
    # Otherwise test the primeness of the rotations
    else:
        allPrimes = True
        rotations = []

        # For each rotation test if it is prime
        # If it prime remove it from the list of primes to test
        # If it is not prime only remove the prime currently tested
        for j in xrange(len(si)):
            si = si[1:] + si[0]
            rotations.append(si)

            if (not int(si) in primes):
                allPrimes = False
                primes.remove(primes[0])
                break
            else:
                primes.remove(int(si))

        # If all rotations were primes add them to the result list
        if (allPrimes):
            res += rotations
            print res

res= list(set([int(i) for i in res]))
res.sort()
print res

print "number of primes: " + str(len(res))
