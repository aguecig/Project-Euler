# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:51:29 2019

@author: aguec
"""

# returns the prime numbers up to integer n

import math

def primes(n):
    primes = [2,3]
    for i in range(5,n,2):
        primality = True
        for j in range(3,int(math.sqrt(i)) + 1,2):
            if i%j == 0:
                primality = False
                break
        if primality == True:
            primes.append(i)
    
    return primes