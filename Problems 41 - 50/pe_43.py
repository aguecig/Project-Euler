# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:12:45 2019

@author: aguec
"""

import itertools

pandigitals = list(itertools.permutations('0123456789',10))
prime_pandigitals = []
primes = [2,3,5,7,11,13,17]

for i in range(len(pandigitals)):
    if pandigitals[0] == '0':
        continue
    else:
        test = True
        for u in range(7):
            if int(pandigitals[i][1+u]+pandigitals[i][2+u]+pandigitals[i][3+u]) % primes[u] != 0:
                test = False
                break
        if test == True:
            prime_pandigitals.append(pandigitals[i])

primedigitals = []

for j in range(len(prime_pandigitals)):
    number = ''
    for k in range(10):
        number = number + prime_pandigitals[j][k]
    primedigitals.append(int(number))

print(primedigitals)
print(sum(primedigitals))