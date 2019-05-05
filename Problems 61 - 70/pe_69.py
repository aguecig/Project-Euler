# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:05:48 2019

@author: aguec
"""

import timeit

start = timeit.default_timer()

# Euler's Totient Function 
def phi(n): 
      
    # Initialize result as n 
    result = n
  
    # Consider all prime factors 
    # of n and subtract their 
    # multiples from result 
    p = 2
    while(p*p <= n): 
          
        # Check if p is a  
        # prime factor. 
        if (n%p == 0):  
              
            # If yes, then  
            # update n and result 
            while (n%p == 0): 
                n = int(n/p) 
            result -= int(result/p) 
        p += 1
  
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most  
    # one such prime factor) 
    if (n > 1): 
        result -= int(result / n)
    return result

ratio = [0,0]
for i in range(2,1000001,2):
    test = i/phi(i)
    if test > ratio[1]:
        ratio = [i,test]

print(ratio)

finish = timeit.default_timer()

print('runtime: ',finish-start,'seconds')