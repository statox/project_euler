#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler

import string
import re
import itertools

# Return the sum of the alphabetical position of each letters of a word
def wordValue(word):
    return sum([string.uppercase.index(c) +1 for c in word])

# Get each word of the file in a list (remove the ")
def readWords(fileToRead):
    with open(fileToRead, 'r') as f:
        return f.read().replace('"', '').split(',')

def main():
    # Read words as a list
    words = readWords('./words.txt')

    # We need a limit for the largest triangular number to generate
    # So we take the longest word of the list, and replace all the letters by 'Z'
    # This will give the largest number to generate
    longestWord = max(words, key=len)
    longestWord = re.sub('.', 'Z', longestWord)
    largestValue = wordValue(longestWord)

    # Get the list of triangular numbers lower than the largest value
    triangulars = [ utilsEuler.triangular(i) for i in itertools.takewhile(lambda x: utilsEuler.triangular(x) <= largestValue, range(1, 1000))]

    # For each word of the list test if it is triangular
    triangularWords = len([w for w in words if wordValue(w) in triangulars])

    print "number of triangular words: " + str(triangularWords)

main()
