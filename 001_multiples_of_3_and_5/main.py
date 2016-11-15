#!/usr/bin/env python
 

def main():
    # Compute sum of multiples of 3 and 5 below 1000

    sum = 0
    multiples = []
    for i in range(0, 1000):
        if (i%3 == 0 or i%5 == 0):
            multiples.append(i)
            sum += i

    print("multiples: " + str(multiples))
    print("sum: " + str(sum))


main()
