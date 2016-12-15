#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

# Brute force version with an arbitrary limit
# A new version should determine when the program has to stop

# Get two indexes a and b, generate the corresponding pentagonal numbers
# And test if their sum and their difference is also pentagonal
def coupleFitsTheProperties(a, b):
    penA = utilsEuler.getPentagonal(a)
    penB = utilsEuler.getPentagonal(b)

    if (utilsEuler.isPentagonal(penA + penB) and utilsEuler.isPentagonal(penA - penB)):
        return True

    return False

def main():
    minDistance = sys.maxint
    keepA = 0
    keepB = 0

    for a in range(1, 3000):
        # print "a: " + str(a)
        for b in range(1, a):
            if (a!=b and coupleFitsTheProperties(a, b)):

                dist = abs(utilsEuler.getPentagonal(a) - utilsEuler.getPentagonal(b))

                if (dist < minDistance):
                    minDistance = dist
                    keepA = utilsEuler.getPentagonal(a)
                    keepB = utilsEuler.getPentagonal(b)
                    print "new min dist: " + str(minDistance)

    print "Smallest distance: " + str(minDistance) + " for " + str(keepA) + " " + str(keepB)

main()
