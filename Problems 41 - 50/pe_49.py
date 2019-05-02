# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:17:52 2019

@author: aguec

"""

import math
from collections import Counter
import timeit

start = timeit.default_timer()

# First construct a list of primes up to 10000

primes = [2,3]

for i in range(5,10000,2):
    primality = True
    for j in range(3,int(math.sqrt(i)) + 1,2):
        if i%j == 0:
            primality = False
            break
    if primality == True:
        primes.append(i)

# extract primes of length 4

d4primes = []

for x in range(len(primes)):
    if len(str(primes[x])) == 4:
        d4primes.append(primes[x])

# Find sets of primes that are permutations of eachother

candidates = []
used = []
for r in range(len(d4primes)):
    if d4primes[r] in used:
        continue
    temp = []
    v1 = str(d4primes[r])
    for s in range(r+1,len(d4primes)):
        v2 = str(d4primes[s])
        if Counter(v1) == Counter(v2):
            used.append(v2)
            temp.append(v2)
    candidates.append(temp)

# extract the permutations that are in groups of 3

threes = []
    
for m in range(len(candidates)):
    if len(candidates[m]) == 3:
        threes.append(candidates[m])

# find which of these groups of 3 are seperated by the same difference value

for n in range(len(threes)):
    if (int(threes[n][1])-int(threes[n][0])) == (int(threes[n][2])-int(threes[n][1])):
        print(threes[n])
        print(threes[n][0] + threes[n][1] + threes[n][2])

finish = timeit.default_timer()

print('run time: ', finish - start, ' seconds')