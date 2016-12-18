#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

# Defines if the string s2 is a permutation of the string s1
def isPermutation(s1, s2):
    if (len(s1) != len(s2)):
        return False

    # Get the characters of s1 without duplicate
    chars = ''.join(set(s1))
    for c in chars:
        if (s1.count(c) != s2.count(c)):
            return False

    return True

def main():
    # Get 4 digits primes
    primes = [x for x in utilsEuler.eratosthenesGenerator(10000) if len(str(x))==4]

    # Get the primes p where (p + 3330) and (p + 6660) are also prime
    # and are a permutation of p
    for p in primes:
        p1 = p + 3330
        p2 = p + 6660
        if (isPermutation(str(p), str(p1)) and isPermutation(str(p), str(p2)) and p1 in primes and p2 in primes):
            print str(p) + '    ' + str(p1) + '    ' + str(p2) + '  -> ' + str(p) + str(p1) + str(p2)

main()
