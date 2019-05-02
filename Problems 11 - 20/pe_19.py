# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:48:45 2019

@author: aguec
"""

months = [31,0,31,30,31,30,31,31,30,31,30,31]
sunday = 0
count = 0
extra = 0

for i in range(1900,2001):
    # in this series of if statements, we work out how many days are in february
    # for each given year
    if i % 400 == 0:
        months[1] = 29
    elif i % 100 == 0:
        months[1] = 28
    elif i % 4 == 0:
        months[1] = 29
    else:
        months[1] = 28
    for j in range(len(months)):
        count = count + months[j]
        if (count + 1) % 7 == 0:
            sunday = sunday + 1
    if i == 1900:      # the problem only wants the sundays from 1901 to 2000, so
        extra = sunday # we must subract the mondays from the year 1900
    
print('The number of Sundays that fell on the first day of the month')
print('from January 01, 1901 to December 31, 2000 is' ,sunday - extra )