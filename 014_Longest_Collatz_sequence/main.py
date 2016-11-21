#!/usr/bin/env python
# -*- coding: utf-8 -*-

def collatz(n):
    count = 1

    while (n != 1):
        count += 1
        if (n % 2== 0):
            n = n / 2
        else:
            n = 3*n + 1

    return count

def search(limit):
    maxI = 0
    maxCount = 0
    for i in range(1, limit):
        newCount = collatz(i)

        if (newCount > maxCount):
            maxCount = newCount
            maxI = i

    print "max: " + str(maxCount)
    return [maxCount, maxI]

res = search(1000000)

print "max i: " + str(res[1])
print "max count: " + str(res[0])
