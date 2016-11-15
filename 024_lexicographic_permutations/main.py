#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# Recursively find permutations
# When the 1000000th is found print it
def permute(n):
    if (len(n) == 2):
        return [str(n), str(n[1]+n[0])]
    else:
        list = []
        for i in n:
            sub = permute(re.sub(i, '', n))

            for s in sub:
                list.append(i + s)
                if (len(list) == 1000000):
                    print "1000000th permutations: " + i+s

        return list

def main():
    permutations = permute("0123456789")

    print str(len(permutations)) + " permutations found"

main()
