# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:51:14 2019

@author: aguec
"""

from math import sqrt
primes = [2,3]
summ = 5
for i in range(5,2000000,2):
    primality = True
    for j in range(3,int(sqrt(i))+1,2):
        if i%j == 0:
            primality = False
            break
    if primality == True:
        primes.append(i)
        summ += i

print(summ)