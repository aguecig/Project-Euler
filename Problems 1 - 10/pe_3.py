# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:38:35 2019

@author: aguec
"""

from math import sqrt
n = 600851475143 
primes = [2,3]
for i in range(5,100000,2):
    primality = True
    for j in range(3,int(sqrt(i))+1,2):
        if i%j == 0:
            primality = False
            break
    if primality == True:
        primes.append(i)
        
for k in range(len(primes)):
    if n%primes[k] == 0:
        print(primes[k])