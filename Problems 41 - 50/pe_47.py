# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:48:32 2019

@author: aguec
"""

import math
primes = [2,3]

for i in range(5,1001,2):
    primality = True
    for j in range(3,int(math.sqrt(i))+1,2):
        if i%j == 0:
            primality = False
            break
    if primality == True:
        primes.append(i)

count = 0

for k in range(10000,500000):
    if k in primes:
        count = 0
        continue
    distinct = 0
    for u in range(len(primes)):
        if primes[u] > k/2 + 1:
            break
        elif k%primes[u] == 0:
            distinct = distinct + 1
    if distinct >= 4:
        count = count + 1
    else:
        count = 0
    if count == 4:
        print(k-3)
        break