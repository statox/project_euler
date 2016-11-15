#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    i = 20
    found = False

    while (not found):
        i += 20
        hasRemainder = False
        divisor=1

        print(str(i))
        while (divisor < 20 and not hasRemainder):
            divisor += 1
            hasRemainder = not (i%divisor == 0)

        if (not hasRemainder):
            found = True

main()
