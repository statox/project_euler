#!/usr/bin/python3
# -*- coding: utf-8 -*-

import functools
import math

# Use python3 feature lru_cache to improve the performence
# of the factorial calculations
@functools.lru_cache(maxsize=None)
def cachedFactorial(n):
    return math.factorial(n)

# Calculate all of the combinations.
# Thanks to the cache function the program is pretty fast
count = 0
for n in range(1, 101):
    fN = cachedFactorial(n)

    for r in range(1, n+1):
        fR = cachedFactorial(r)
        fDIFF = cachedFactorial(n-r)

        if (fN / (fR * fDIFF) > 1000000):
            print(str(n) + "C" + str(r) + "\t= " + str(fN / (fR * fDIFF)))
            count += 1

print("Result: " + str(count))
