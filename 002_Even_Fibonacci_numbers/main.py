#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    # Compute sum of even Fibonacci number

    prev=1
    current=2
    sum=2

    while (current < 4000000):
        tmp=prev+current
        if (tmp%2 == 0 and tmp < 4000000):
            sum += tmp

        prev=current
        current=tmp

    print("sum: " + str(sum))

main()
