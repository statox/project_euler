#!/usr/bin/env python
# -*- coding: utf-8 -*-

# We can observe that the number of lattice path for a grid of nxn is the value
# of the middle of the line 2n of the pascal triangle
#
# for the first possible grids:
# grid 1x1 = 2 paths = pascal line 2 = 1 2 1
# grid 2x2 = 4 paths = pascal line 4 = 1 4 6 4 1
# grid 3x3 = 20 paths = pascal line 6 = 1  6  15  20  15  6  1 
#
# For a grid 20x20 we need to generate the 40th line of the pascal triangle and
# take its middle value (or more easily the max value)

def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n-k) / (k+1))
    return line

print max(pascal(40))
