#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We loop on 1, 1000 to get every i^i numbers
# We keep only the last 10 digits of this numbers and
# add them to the total. (We also only keep the last 10 digits
# of the total)
def main():
    total=0
    for i in range(1, 1001):
        iPow = pow(i, i)
        lastDigits = int(str(iPow)[-10:])

        total += lastDigits
        total = int(str(total)[-10:])

        print str(i)

    print "last 10 digits: " + str(total)

main()
