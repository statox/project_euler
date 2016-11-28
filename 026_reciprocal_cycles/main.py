#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *

def tortoiseHare(s):
    print "TH: " + s
    # Main phase: find a repetition x_i=x_2i
    i=1

    tortoise = s[i]
    hare = s[2*i]

    while (tortoise != hare and 2*i < len(s)-1):
        i += 1
        tortoise = s[i]
        hare = s[2*i]
        # print str(i) + "\tt: " + str(tortoise) + "\th: " + str(hare)
        # raw_input()

    if ( 2*i == len(s)-2):
        print "no cycle"
    else:
        print "position t: " + str(i) + "\tdistance: " +str((2*i)-i)


    # Find the position μ of first repetition.    
    mu = 0
    j = 0
    tortoise = s[j]
    while (tortoise != hare):
        j += 1
        i += 1

        tortoise = s[j]
        hare = s[i]

        mu += 1

    print "mu : " + str(mu)


    # Find the length of the shortest cycle starting from x_μ
    lam = 1
    tortoise = s[mu]
    i = mu+1
    hare = s[i]

    print "tortoise: " + str(tortoise) + "\t" + "hare: " + str(hare)
    while (tortoise != hare):
        i += 1
        hare = s[i]
        lam += 1

    print "lam: " + str(lam)


def main():
    getcontext().prec = 50
    for i in range(2, 20):
        s = str(1/Decimal(i))

        if (len(s) <= 7):
            s+="0000000000000000000000"

        tortoiseHare(s[2:])


main()
