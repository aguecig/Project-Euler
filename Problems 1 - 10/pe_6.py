# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:43:45 2019

@author: aguec
"""

summ = 0
square_summ = 0

for i in range(1,101):
    summ += i
    square_summ += i**2
    
sum_square = summ**2

print(abs(sum_square - square_summ))