#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Let's be lazy let's bruteforce that
def searchTriplet():
    c=b=a=0
    found = False

    while (True):
        c += 1

        print "c: " + str(c)
        for b in range(1, c):
            for a in range(1, b):
                if (( a + b + c == 1000 ) and ( a*a + b*b == c*c )):
                    return [a, b, c]

triplet = searchTriplet()
print "Triplet: " + str(triplet)

print "product: " + str(triplet[0]*triplet[1]*triplet[2])
