#!/usr/bin/env python
# -*- coding: utf-8 -*-

def isPal(n):
    if (len(str(n))%2==0):
        return str(n)[:len(str(n))/2] == str(n)[len(str(n))-1:len(str(n))/2-1:-1]
    else:
        return str(n)[:len(str(n))/2] == str(n)[len(str(n))-1:len(str(n))/2:-1]

def main():
    max = 0
    for i in range(999, 100, -1):
        for j in range (999, 100, -1):
            if (isPal(i*j) and max<i*j):
                max = i*j
                print(str(i) + " x " + str(j) + " = " + str(i*j))

    print("Max: " + str(max))


main()
