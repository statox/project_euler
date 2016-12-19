#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This version could maybe be improved.
# I'm not sure the stop condition is correct
def main():
    p = 0
    prevCount = -1
    count = 0
    while (True):
        p += 1
        i = 0

        while (len(str(i**p)) <= p):
            i += 1
            # print "\t" + str(i) + "\t" + str(i**p)
            if (len(str(i**p)) == p):
                count += 1

        print str(p) + " \tcount: " + str(count) + "\ti: " + str(i)

        if (prevCount != count):
            prevCount = count
        else:
            break

    print "result: " + str(count)

main()
