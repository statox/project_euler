#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler
import time
import itertools

# First version: Generate all the cubes between 5^3 and 10000^3 (arbitrary limit)
# For each cube compare it to all of the other cubes to see if they are permutations
# When a cube with 5 permutations is found (4 permutations + itself) the algorithm stops
# That's not really efficient since the complexity is O(n^2) (I think)
#
# Execution time: ~79 seconds
def v1():
    cubes = []
    prevLen = 0
    for i in range(5, 10000):
        cubes.append(i*i*i)

    for k in cubes:
        permuts = 0
        for j in [x for x in cubes if x != k]:
            if (utilsEuler.isPermutation(str(k), str(j))):
                permuts += 1
            if (permuts == 4):
                print "Smallest cube found: " + str(k)
                return

        # if (len(str(k)) > prevLen):
            # prevLen = len(str(k))
            # print "Testing cubes of len " + str(prevLen)

    print "not found"

# Second version: This version is improved since it groups the cubes of the same size
# We don't need an arbitrary high limit anymore and each cube is compared to less cubes
# than in the previous version
#
# Execution time: ~39 seconds
def searchPermutations(cubes):
    for k in cubes:
        permuts = 0
        for j in [x for x in cubes if x != k]:
            if (utilsEuler.isPermutation(str(k), str(j))):
                permuts += 1
            if (permuts == 4):
                return k

    return -1

def v2():
    i = 0
    cubes = [1]
    found = False
    while (not found):
        i += 1

        c = i*i*i
        if (len(str(c)) > len(str(cubes[-1]))):
            res = searchPermutations(cubes)
            if (res != -1):
                found = True
                print "Smallest cube found: " + str(res)
            # else:
                # print "Smallest cube not found among " + str(len(cubes)) + " cubes of len " + str(len(str(cubes[-1])))
            cubes = [c]
        else:
            cubes.append(c)

# Third version: Better version!
# Each cube is tested only once: For each cube we sort its string representation and
# use this reprensentation a key in a dicitonnary.
# Each time a key is encountered, we increment its value. The first key which has 5 as
# its value is the cube we are looking for.
# When we create a key we also keep the cube which generated it since it will be our answer
#
# Execution time: ~1.1 seconds
def v3():
    permutations = {}
    prevLen=0

    for i in (x**3 for x in itertools.count(1)):
        c = ''.join(sorted(str(i)))

        # if (len(c) > prevLen):
            # prevLen = len(c)
            # print "Testing cubes of len " + str(prevLen)

        if (c in permutations.keys()):
            permutations[c][1] += 1
        else:
            permutations[c] = [i, 1]

        if (permutations[c][1] == 5):
            print "Smallest cube found: " + str(permutations[c][0])
            break

def main():
    start=time.time()
    v1()
    end=time.time()
    tv1 = end-start
    print "Time of v1 : " + str(tv1)

    start=time.time()
    v2()
    end=time.time()
    tv2 = end-start
    print "Time of v2 : " + str(tv2)

    start=time.time()
    v3()
    end=time.time()
    tv3 = end-start
    print "Time of v3 : " + str(tv3)


main()
