# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:50:42 2019

@author: aguec
"""

f0 = 0
f1 = 1

L = 1
count = 1
while L < 1000:
    temp = f1
    f1 = f1 + f0
    f0 = temp
    L = len(str(f1))
    count = count + 1
    
print(count)