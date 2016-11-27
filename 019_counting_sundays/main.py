#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For a reason that I don't understand the program counts
# one sunday more than the searched value

# Contains 'True' when leap[1900+i] is a leap year
leap = [((y % 4 == 0 and y % 100 != 0) or (y % 100 == 0 and y % 400 == 0)) for y in xrange(1900, 2001)]

nameOfMonth = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

i = -1
nbOfSunday = 0

for year in xrange(len(leap)):
    # Update number of days in february
    if (leap[year]):
        months[1] = 29
    else:
        months[1] = 28

    for month in xrange(len(months)):
        for day in xrange(1, months[month]+1):
            i += 1
            dow = days[i%7]

            if (day == 1 and dow == 'Sunday' and year > 0):
                nbOfSunday += 1
                print str(1900+year) + "\t" + nameOfMonth[month] + "\t" + str(day) + "\t" + dow

            # If I uncomment these line, the number of sundays is correct
            # if (year == 10 and month == 11 and day == 25):
                # break

print "Number of sundays first day of the week: " + str(nbOfSunday)
