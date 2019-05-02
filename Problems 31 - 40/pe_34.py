# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:43:30 2019

@author: aguec
"""

import math
facts = []

for i in range(10,500000):
    summ = 0
    for j in range(len(str(i))):
        summ = summ + math.factorial(int(str(i)[j]))
    if summ == i:
        facts.append(i)
            
print(facts)
print(sum(facts))