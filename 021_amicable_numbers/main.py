#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

# amicables_test=[220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
# result=31636

def main():
    # Get sum of proper divisors for each natural in 0, 10000
    d = [sum([i for i in range(1, n) if (n%i==0)]) for n in range(0, 10000)]


    # Get the amicables - one liner
    amicables=[i for i in range(0, len(d)) if d[i] < len(d) and i != d[i] and i == d[d[i]] and d[i] == d[d[d[i]]]]

    # Get the amicables - long version
    # for i in range(0, len(d)):
        # if (d[i] < len(d) and i != d[i] and i == d[d[i]] and d[i] == d[d[d[i]]]):
            # amicables.append(i)

    res = sum(amicables)
    print("result: " + str(res))

main()
