#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isPandigital(i):
    panString = str(i)

    # don't test strings with a 0 or less than 9 digits
    if ('0' not in panString and len(panString) == 9):
        # Remove duplicates to see if this is a pandigital
        noDuplicate = "".join(set(panString))

        if (len(noDuplicate) == 9):
            return True

    return False

maxPan = 0
# The limit for n to test is 9999
# because over this limit n * 2 has more than 9 characters
for i in range(1, 10000):
    res = ""
    for j in range(1, 10):
        res += str(i*j)

        if (len(res)==9 and isPandigital(res)):
            print str(i) + "\t* " + str([k for k in range(1, j+1)]) + "\t=" + res

            if (int(res) > maxPan):
                maxPan = int(res)

        elif (len(res) > 9):
            break

print "max " + str(maxPan)
