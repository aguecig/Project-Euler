# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:51:47 2019

@author: aguec
"""

import math

primes = [2,3]

for i in range(5,1000000,2):
    primality = True
    for j in range(3,int(math.sqrt(i))+1,2):
        if i%j == 0:
            primality = False
            break
    if primality == True:
        primes.append(i)

candidates = []
for m in range(len(primes)):
    count = 0
    summ = 0
    for k in range(m,len(primes)):
        count = count + 1
        summ = summ + primes[k]
        if summ > primes[-1]:
            break
        elif count > 500 and summ in primes:  #this is the line in the program that I
            candidates.append([summ,count])   #adjusted to make the list of candidates
                                              #less entropic.
                                            

def my_max(x):
    maximum = 0
    prime = 0
    for r in range(len(x)):
        if x[r][1] > maximum:
            maximum = x[r][1]
            prime = x[r][0]
    return prime,maximum

print('Prime and consecutive prime sums respectively\
          ',my_max(candidates))