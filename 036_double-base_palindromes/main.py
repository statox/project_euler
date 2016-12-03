#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

sumPal = 0
for i in range(1, 1000000):
    if (utilsEuler.isPalindrome(str(i)) and utilsEuler.isPalindrome(str(bin(i))[2:])):
        sumPal += i
        print str(i) + "\t" + str(bin(i))[2:]

print "Final sum: " + str(sumPal)
