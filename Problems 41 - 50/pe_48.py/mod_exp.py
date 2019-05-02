# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:40:11 2018

@author: aguec
"""

#This program runs modular exponentiation in log(e) time.

# ex: 439^652 mod 673 = 147

# b is the base
# e is the exponent
# n is the modulus

def mod_exp(b,e,n):
    base = b  #saving original value of b and e for the final print statement
    exponent = e
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
    
    #print(base,'^',exponent,'mod(',n,') = ',b)
    
    return b