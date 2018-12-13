#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('../utils'))
import utilsEuler
import string
import operator

# I used the following code to decipher the text with each possible keys
# (aaa, aab, aac, ... , zzz)
# When I saw the first results, I decided to decipher only the first 15
# characters of the text and to grep for the word "The" (ignoring the case)
# This only gave one matching key: god
#
# From that I created solver.py to get the correct answer

def main():
    # Reading the number in the cipher file as integers
    readBytes = []
    with open('./p059_cipher.txt', 'r') as f:
        print("Reading the cipher")
        readBytes = [int(x) for x in f.readline().strip().split(',')]

    # Only keep the beginning of the text
    readBytes = readBytes[0:15]

    print("Generating the keys")
    keys = []
    for i in range(ord('a'), ord('z')+1):
        for j in range(ord('a'), ord('z')+1):
            for k in range(ord('a'), ord('z')+1):
                keys.append([i, j, k])

    print("Decyphering with each key")
    for keyDigits in keys:
        key = "".join([chr(x) for x in keyDigits])
        result = ""

        for i in range(0, len(readBytes)):
            result += chr(readBytes[i] ^ keyDigits[i % len(keyDigits)])

        print(key, result)

main()
