# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 23:11:40 2019

@author: aguec
"""

import mod_exp

# for the project euler problem, the input should be:
# n = 1000
# last = 10000000000 = 10**10

def self_powers(n,last):
    
    summ = 0
    for i in range(1,n+1):
        summ = summ + mod_exp.mod_exp(i,i,last)
        
    print(summ%10**10)