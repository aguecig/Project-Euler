# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:42:41 2019

@author: aguec
"""

import math

file = open('pe_99.txt','r')

values = []

for lines in file:
    values.append(lines)

numbers = []

# get the data of bases and their corresponding exponents and put them into 
# a data array of integers

for i in range(len(values)):
    base = ''
    exp = ''
    g = 0
    for j in range(len(values[i])):
        if values[i][j] == ',':
            g = 1
            continue
        elif g == 0:
            base = base + values[i][j]
        elif g == 1:
            exp = exp + values[i][j]
    numbers.append([int(base),int(exp)])
    
# now to find the largest answer, it takes far too much work to just calculate
# each base with its exponential. So instead, we take note of the following
# relationship:
    
' if     b^x > u^v '
' then   x*log(b) > v*log(u) '

# computationally it is much easier to work with logs, and so this is how we
# approach the rest of the problem.

big = 0
line = 0

for k in range(len(numbers)):
    test = numbers[k][1]*math.log(numbers[k][0])
    if test > big:
        big = test
        line = k + 1

print('The line in the file with the largest value is: ',line)

file.close()