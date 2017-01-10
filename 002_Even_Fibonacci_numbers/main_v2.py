#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generate first numbers of fibonnaci sequence lower than limit
def fibLimit(limit):
    l = [0, 1]
    while l[-1] + l[-2] <= limit: l.append(l[-1] + l[-2])

    return l

# Compute sum of even Fibonacci number
print 'sum:', sum([i for i in fibLimit(4000000) if i%2 == 0])
