# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:49:00 2019

@author: aguec
"""

from math import sqrt
primes = [2,3]
for i in range(5,1000000,2):
    primality = True
    for j in range(3,int(sqrt(i))+1,2):
        if i%j == 0:
            primality = False
            break
    if primality == True:
        primes.append(i)
        
print(primes[10000])