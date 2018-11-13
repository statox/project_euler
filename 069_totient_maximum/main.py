#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import sys
import os
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

from collections import deque

# def phi(n):
    # numberOfRelativePrimes=0;

    # for i in range(1, n):
        # if (utilsEuler.gcd(i, n) == 1):
            # numberOfRelativePrimes += 1

    # return numberOfRelativePrimes;

# maxRatio = 0
# for n in range(2, 1000001):
# # for n in range(2, 10):
    # relPrimes = phi(n);
    # ratio = n/relPrimes

    # if (ratio > maxRatio):
        # maxRatio = ratio;
        # print ("new max. n:", n, "ratio", ratio);

    # if (n % 10000 == 0):
        # print("We are at", n);

def nextGen(( m, n )):
    return [(2*m + n, m), (2*m - n, m), (m + 2*n, n)]

stop=False;
tuples=deque();
tuples.append((2, 1));
tuples.append((3, 1));
LIMIT=15
# LIMIT=1000000

coprimes = dict();

maxRatio = 0
maxRatioN = 0

# First generate all the pairs of coprimes under LIMIT
# and create a dictionnary coprimes with a number as key and its coprimes as values
# See https://en.wikipedia.org/wiki/Coprime_integers#Generating_all_coprime_pairs
#
# TODO: to improve the performence of the algorithm I think on each step
# we can remove the keys which are smaller than the smallest number in the generated tuples
# this way we don't need to keep a huge dictionnary and thus looking for its key should be faster
# TODO: Actually the real problem is to define when we can calculate the ratio of a number
# i.e. when we are sure that it will not appear in a tuple anymore
while(len(tuples) > 0):
    current = tuples.popleft()
    # print(current)
    [ tuples.append(res) for res in nextGen(current) if res[0] <= LIMIT]

    if current[0] in coprimes:
        coprimes[current[0]].append(current[1])
    else:
        coprimes[current[0]] = [ current[1] ]

# Once we all have them we can calculate the ratio for every number under LIMIT
# and get the one with the biggest ratio
for n in coprimes:
    ratio = n / len(coprimes[n])

    if (ratio > maxRatio):
        maxRatio = ratio
        print("new max ratio. n:", n, "ratio", ratio)

# print(coprimes)
