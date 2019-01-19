# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:08:19 2019

@author: aguec
"""

import math
candidates = [3,5,7]

for i in range(11,800000):
    if '0' in str(i):
        continue
    if '2' in str(i):
        continue
    if '4' in str(i):
        continue
    if '5' in str(i):
        continue
    if '6' in str(i):
        continue
    if '8' in str(i):
        continue
    else:
        test = True
        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i%j == 0:
                test = False
                break
            else:
                pass
    if test == True:
        candidates.append(i)

trunc_primes = []

for r in range(3,len(candidates)): # don't want to test 3,5 or 7 (they don't count)
    s = str(candidates[r])
    test = True
    for t in range(len(s)):
        if int(s[0+t:len(s)]) not in candidates:
            test = False
            break
        if int(s[0:len(s)-t]) not in candidates:
            test = False
            break
    if test == True:
        trunc_primes.append(candidates[r])

# here we must remember to include the primes 23 and 53, which are not included
# in the algorithm by design.
trunc_primes.append(23)
trunc_primes.append(53)
print(trunc_primes)
print(sum(trunc_primes))