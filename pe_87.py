# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:02:11 2019

@author: aguec
"""

# the fourth root of 50 000 000 is ~ 84
# the cube root of 50 000 000 is ~ 368
# the square root of 50 000 000 is ~7071

import timeit

start = timeit.default_timer()

import math
primes = [2,3]

for i in range(5,7072,2):
    primality = True
    for j in range(3,int(math.sqrt(i)) + 1,2):  #forgot the +1 originally...
        if i%j == 0:
            primality = False
            break
    if primality == True:
        primes.append(i)
        
prime_squares = [primes[r]**2 for r in range(len(primes))]
prime_cubes = []
s = 0
while primes[s]**3 < 50000000:
    prime_cubes.append(primes[s]**3)
    s = s + 1
prime_fourths = []
t = 0
while primes[t]**4 < 50000000:
    prime_fourths.append(primes[t]**4)
    t = t + 1
    
#print(prime_squares)
#print(prime_cubes)
#print(prime_fourths)
    
prime_sums = []
    
for x in range(len(prime_squares)):
    for y in range(len(prime_cubes)): 
        for z in range(len(prime_fourths)):
            summ = prime_squares[x] + prime_cubes[y] + prime_fourths[z]
            if summ >= 50000000:
                continue
            else:
                prime_sums.append(summ)
    
print(len(set(prime_sums))) 

stop = timeit.default_timer()

print('Run time: ',stop - start,' seconds')