# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 21:55:03 2019

@author: aguec
"""

import math

# b must be prime for the equation to produce a prime at n = 0, so we first 
# generate the list of primes up to 1000

b = [2,3]

for i in range(5,999,2): # checking only odd values
    prime = True
    for j in range(2,int(math.sqrt(i) + 1)):
        if i%j == 0:
            prime = False
            break
        else:
            pass
    if prime == True:
        b.append(i)
        
a = [k for k in range(-999,1000)]

record = 0

for r in range(len(a)):
    for s in range(len(b)):
        streak = 0
        n = 0
        while (n**2+a[r]*n+b[s]) in b:
            streak = streak + 1
            n = n + 1
        if streak > record:
            record = streak
            coefficients = (a[r],b[s])
            
print('longest streak of primes is: ', record)
print('equations that produces longest streak is: n**2 + ',coefficients[0],'n + ',coefficients[1])
print('product of coefficients that produce the longest streak is: ',a[r]*b[s])