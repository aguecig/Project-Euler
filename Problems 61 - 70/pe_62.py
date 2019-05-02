# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:08:50 2019

@author: aguec
"""

import timeit

start = timeit.default_timer()

from collections import Counter

# initialize lists and integers
cubes = []  # this list keeps track of the cubes 
counts = [] # this list keeps track of how each cube can be permutated
size = 0
result = 0


for i in range(405,10000):
    add = False
    stest = str(i**3)
    if len(stest) > size: # if the next cube has more digits than the previous
        cubes = []        # cube, then it can't be a permutation. So we reset
        counts = []       # the lists and set the new size and start again.
        size = len(stest)
        continue
    if Counter(stest) in counts:            # See if the cube is already a 
        for j in range(len(counts)):        # permutation of another cube in the
            if Counter(stest) == counts[j]: # counts list so far. 
                add = True
                save = j
                break
    counts.append(Counter(stest))                
    cubes.append([i**3,1])
    if add == True:                         # if the cube is just a permutation 
        cubes[save][1] = cubes[save][1] + 1 # of a cube already in the list, 
        if cubes[save][1] == 5:             # we add one to the original cubes
            result = cubes[save]            # score. Once it reaches a score of 5,
            break                           # we know the answer to the problem.
            
print(result)

stop = timeit.default_timer()

print('Time taken to run program: ', stop - start, ' seconds.')