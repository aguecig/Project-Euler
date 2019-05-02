# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 19:46:39 2019

@author: aguec
"""

import math

candidates = []

for i in range(5,10000000,2):
    s = str(i)
    if '0' in str(i): # cannot have a zero in a pandigital number
        continue
    elif set(s) != set(str(j) for j in range(1,len(s) + 1)): # check to see if
        continue                                             # the number is
    else:                                                    # pandigital first 
        test = True
        for k in range(3,int(math.sqrt(i) + 1),2):   # now check primality
            if i%k == 0:
                test = False
                break
            else:
                pass
        if test == True:
            candidates.append(i)

print(max(candidates))