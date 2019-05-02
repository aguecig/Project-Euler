# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:17:57 2019

@author: aguec
"""

'Goldbachs Failed Conjecture'
'Conjecture: every odd composite number can be written as the sum of a prime and twice a square.'
'This program finds the first odd integer not prime for which this statement is false.'

import math

primes = [2,3]

for i in range(5,10000,2):
    primality = True
    for j in range(3,int(math.sqrt(i))+1,2):
        if i%j == 0:
            primality = False
            break
    if primality == True:
        primes.append(i)

numbers = [a for a in range(1,10001)]

for k in range(9,10002,2):
    x = 0
    test = True
    if k in primes:
        continue
    else:
        for u in range(len(primes)):
            if x == 1:
                break
            elif primes[u] > k:
                test = False
                break
            else:
                for v in range(len(numbers)):
                    if primes[u] + 2*numbers[v]**2 > k:
                        break
                    elif primes[u] + 2*numbers[v]**2 == k:
                        test = True
                        x = 1
                        #print([k,primes[u],numbers[v]])
                        break
                    elif primes[u] + 2*numbers[v]**2 < k:
                        continue
        if test == True:
            continue
        elif test ==  False:
            print(k)
            break