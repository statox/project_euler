#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Doesn't work: too many recursion levels
def fib(n1, n2):
    new = n1 + n2
    print str(new)
    if len(str(new)) > 1000:
        print "Found: " + str(new)
        return new
    else:
        fib(n2, new)

# Works great and fast
def fibLin():
    n1 = 0
    n2 = 1
    new = 1
    index = 1

    while (len(str(new)) < 1000):
        index += 1
        new=n1+n2
        n1=n2
        n2=new

    print "Found: " + str(new)
    print "At index: " + str(index)

def main():
    fibLin()

main()
