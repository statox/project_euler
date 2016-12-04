#!/usr/bin/env python
# -*- coding: utf-8 -*-

# That is a first version which can be improved.
# In this one we store in memory each integer in the string
#
# A better version would be to generate the integers and get the dn
# on the fly without storing them.

### Version 1
# Concatenate integers untils the string is 1000000 characters long
strI=""
i=0
while (len(strI) < 1000000):
    i += 1
    strI += str(i)

# Get each dn to find and multiply then
nsToTest = [1, 10, 100, 1000, 10000, 100000, 1000000]
prod = 1
for n in nsToTest:
    prod *= int(strI[n-1])
    print strI[n-1]

# Result
print "prod: " + str(prod)
