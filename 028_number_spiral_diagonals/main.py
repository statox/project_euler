#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Diagonal NE: 4*n*n - 4n  + 1
# Diagonal NW: 4*n*n - 6n  + 3
# Diagonal SE: 4*n*n - 10n + 7
# Diagonal SW: 4*n*n - 8n  + 5

# Get the number of each half diagonal
gridSize = 1001
diagonalSize = (gridSize / 2) + 1

# For sum each number on each diagonal
sumDiagonal = 0
for n in xrange(1, diagonalSize+1):
    sumDiagonal += 4*n*n - 4 * n  + 1
    sumDiagonal += 4*n*n - 6 * n  + 3
    sumDiagonal += 4*n*n - 10 * n + 7
    sumDiagonal += 4*n*n - 8 * n  + 5

# Remove 3 additional 1
sumDiagonal -= 3

print "grid: " + str(gridSize) + "\t sumDiagonal: " + str(sumDiagonal)
