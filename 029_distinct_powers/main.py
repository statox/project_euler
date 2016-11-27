#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

powers=[]

for a in range(2, 101):
    for b in range(2, 101):
        powers.append(pow(a, b))

powers = powers

p = set(powers)
print len(p)
