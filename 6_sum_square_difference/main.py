#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def main():
    sumOfNatural = 0
    sumOfSquares = 0

    for i in range(1, 101):
        print(str(i))
        sumOfNatural += i
        sumOfSquares += math.pow(i, 2)

    sumOfNatural = math.pow(sumOfNatural, 2)
    diff = sumOfNatural - sumOfSquares
    print("sum of natural " + str(sumOfNatural)
            + "\tsum of squares " + str(sumOfSquares)
            + "\tdifference " + str(diff))

main()
