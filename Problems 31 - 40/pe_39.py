# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 19:08:46 2019

@author: aguec
"""

import math
import operator

triples = []
# first we calculate pythogorean triples with hypotenuse less than 1000
for i in range(3,1000):
    for j in range(i,1000):
        c = math.sqrt(i**2 + j**2)
        if c > 1000:
            continue
        elif c%2 == 0:
            triples.append([i,j,c])
        elif (c-1)%2 == 0:
            triples.append([i,j,c])
        else:
            pass
        
p_dict = {}
# now we create a dictionary to keep track of the sums of the perimeters of such
# triangles, and how many times we get the same perimeter
for r in range(1,len(triples)):
    if sum(triples[r]) > 1000:
        continue
    elif sum(triples[r]) not in p_dict:
        p_dict[sum(triples[r])] = 1
    elif sum(triples[r]) in p_dict:
        p_dict[sum(triples[r])] = p_dict[sum(triples[r])] + 1
        
x = max(p_dict.items(), key = operator.itemgetter(1))[0] 
# gets the key in the dictionary with the largest integral value

print(x)