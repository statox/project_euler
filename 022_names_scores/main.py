#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

def main():
    # Get all the names as list items
    f=open('p022_names.txt', 'r')
    list = []
    for line in f:
        list = line.replace('"', '').strip().split(',')
    f.close()

    # For each item get index and score by adding letters position in the alphabet
    list.sort()
    index = 0
    total = 0
    for name in list:
        index += 1
        score = 0
        for letter in name:
            score += 1 + string.uppercase.index(letter)

        score *= index
        total += score
        print(name + " : " + str(score))

    print("total: " + str(total))



main()
