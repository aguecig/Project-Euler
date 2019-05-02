# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 22:45:07 2019

@author: aguec
"""

# we want to find the last 10 digits of 
'28433 × 2^7830457 + 1'
# or in other words:
'28433 × 2^7830457 + 1  mod(10000000000)'

def mod_exp(b,e,n):
    if b >= n:  #reducing the base so that 0 <= b < n
        b = b % n
    store = []
    while e > 0:
        if e == 1:
            for i in range(len(store)):
                b = b*store[i] % n
            e = 0
        elif e % 2 != 0:
            e = (e - 1)/2
            store.append(b)
            b = b**2 % n
        elif e % 2 == 0:
            e = e/2
            b = b**2 % n
    
    return b

pow_2 = mod_exp(2,7830457,10000000000)

total = 28433*pow_2 + 1

final_10_digits = total % 10000000000

print(final_10_digits)