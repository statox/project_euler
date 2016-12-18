#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

def isLychrel(n, i):
    s = str(n + int(''.join(reversed(str(n)))))

    if (utilsEuler.isPalindrome(s)):
        return True
    elif (i > 50):
        return False
    else:
        return isLychrel(int(s), i+1)

lychrels = []
for i in range(1, 10001):
    if (not isLychrel(i, 1)):
        lychrels.append(i)

print lychrels
print "len lychrels: " + str(len(lychrels))
