# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:56:45 2019

@author: aguec
"""

import timeit

start = timeit.default_timer()

import math

def decimal_algorithm(m,n):
    Q = []
    distance = []
    while m not in Q:
        count = 0
        while math.floor(m/n) == 0:
            temp = str(m) + '0'     # if we must add in more zeros, then this
            m = int(temp)           # will show up in the decimal representation
            count = count + 1       # see for example, 1/11 = 0.090909...
        if m in Q:
            break
        Q.append(m)
        if (m/n) % 1 == 0:         # terminate if the decimal is non repeating.
            break
        quotient = math.floor(m/n)
        m = m - quotient*n
        distance.append(count)
    save = 0
    for i in range(len(Q)):       # here we find out when the cycle repeats 
        if Q[i] == m:             # itself
            save = i
    cycle_length = 0
    for j in range(save,len(distance)):           # find the distance of the cycle
        cycle_length = cycle_length + distance[j]
    
    return cycle_length 

lengths = []

for s in range(2,1000):
    lengths.append(decimal_algorithm(1,s))

big = 0
for t in range(len(lengths)):
    if lengths[t] > big:
        big = t + 2          # we add two because we started the algorithm
                             # from the fraction 1/2, but the list indexing 
                             # begins at 0.
print('1 /',big, ' gives the fraction with the largest repeating cycle for a denominator less than 1000')

end = timeit.default_timer()

print('runtime: ', end - start, ' seconds.')