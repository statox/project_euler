#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read the file
l = []
with open('./p059_cipher.txt', 'r') as f:
    l = [int(x) for x in f.readline().strip().split(',')]

# I found the key with some trial and error as detailled in main.py
textKey = 'god'
key = [ord(x) for x in textKey]
print key

# Get the deciphered text by XORing each character with the appropriate character of the key
res = ''
for i in range(0, len(l)):
    res += chr(l[i] ^ key[i % len(key)])
print res

# Get the sum of the ascii values in the decyphered text
total = sum([ord(x) for x in res])
print("answer:", total)
