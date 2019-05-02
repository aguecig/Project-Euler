# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:24:48 2019

@author: aguec
"""

pandigital = []

for m in range(1,5000):
    for n in range(m+1,5000):
        if m*n in pandigital:
            continue              # I was using pass instead of continue here 
        if '0' in str(m):         # and as such, the output was incorrect!
            continue
        elif '0' in str(n):
            continue
        elif '0' in str(m*n):
            continue
        elif len(str(m*n) + str(m) + str(n)) != 9:
            continue
        elif set(str(m*n) + str(m) + str(n)) == {'1','2','3','4','5','6','7','8','9'}:
            pandigital.append(m*n)               # originally, I put this set as integers 
        else:                                    # and not strings, so pandigital was
            pass                                 # returning the empty set.

print(pandigital)
print(sum(pandigital))

