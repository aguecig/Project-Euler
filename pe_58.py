# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:47:54 2019

@author: aguec
"""

from random import randrange

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

def probably_prime(n, k):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.

    """
    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def prime_ratio(n):
    diagonal = [1]
    primes = []
    for i in range(3,n+1,2):
        iv = i**2
        diagonal.append(iv)
        test = probably_prime(iv,10)
        if test == True:
            primes.append(iv)
        
        for j in range(1,4):
            temp = iv - j*(i-1)
            diagonal.append(temp)
            test2 = probably_prime(temp,10)
            if test2 == True:
                primes.append(temp)
    ratio = len(primes)/len(diagonal)
    print(ratio)