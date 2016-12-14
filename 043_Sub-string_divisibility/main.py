#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

# That is a brute force version generating every pandigital numbers,
# removing the ones beginning with '0' and then testing each substring

def hasProperty(n):
    divisors = [2, 3, 5, 7, 11, 13, 17]

    for i in xrange(len(divisors)):
        if (int(n[i+1:i+4]) % divisors[i] != 0):
            return False

    return True

def main():
    print "generating pandigitals"
    pandigitals=[x for x in utilsEuler.permute("0123456789") if x[0] != '0']

    meetCriterion=[int(x) for x in pandigitals if hasProperty(x)]

    print "number of pandigital meeting the criterion: " + str(len(meetCriterion))
    print "sum: " + str(sum(meetCriterion))

main()
