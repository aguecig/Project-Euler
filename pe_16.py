# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:56:17 2019

@author: aguec
"""

#we are finding the sum of the digits that make up b^x.

#for pe_16, b = 2 and x = 1000

def sum_of_digits(b,x):
    number = str(b**x)
    
    summ = 0
    
    for i in range(len(number)):
        summ = summ + int(number[i])
        
    print(summ)