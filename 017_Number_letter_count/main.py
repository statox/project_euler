#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Decompose the number in 100s, 10s and 1s
def decomposeNumber(n):
    number = {}
    if (n>=100):
        number[100]=n/100
        n = n%100
    if (n>= 10):
        number[10]=n/10
        n = n%10
    number[1] = n

    return number

# Based on the decomposition write the number
def writeNumber(numbers, n):
    string = ""

    if (not n.get(100) is None):
        # Handle the edge case of 1000 (I'm too lazy to code it entirely)
        if (n[100] == 10):
            return 'one thousand'
        string += numbers[n[100]] + " hundred "
        if (not n.get(10) is None or (not n.get(1) is None and n[1] > 0)):
            string += "and "

    if (not n.get(10) is None):
        if (n[10] > 1):
            string += numbers[10*n[10]] + " "
        else:
            if (n[10] == 1):
                if (n.get(1) is None):
                    string += "ten"
                else:
                    string += numbers[10*n[10] + n[1]]
                return string

    if (not n.get(1) is None and n[1] > 0):
        string += numbers[n[1]]

    return string

numbers = {
        1    :  'one',
        2    :  'two',
        3    :  'three',
        4    :  'four',
        5    :  'five',
        6    :  'six',
        7    :  'seven',
        8    :  'eight',
        9    :  'nine',
        10   :  'ten',
        11   :  'eleven',
        12   :  'twelve',
        13   :  'thirteen',
        14   :  'fourteen',
        15   :  'fifteen',
        16   :  'sixteen',
        17   :  'seventeen',
        18   :  'eighteen',
        19   :  'nineteen',
        20   :  'twenty',
        30   :  'thirty',
        40   :  'forty',
        50   :  'fifty',
        60   :  'sixty',
        70   :  'seventy',
        80   :  'eighty',
        90   :  'ninety',
        100  :  'hundred'
        }

count = 0
for i in range(1, 1001):
    count += len(writeNumber(numbers, decomposeNumber(i)).replace(" ", ""))
    print str(i) + "  " + writeNumber(numbers, decomposeNumber(i))

print "final count: " + str(count)
