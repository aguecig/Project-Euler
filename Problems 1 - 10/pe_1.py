# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:29:56 2019

@author: aguec
"""

summ = 0
for i in range(1,1000):
    if i%3 == 0 and i%5 != 0:
        summ += i
    elif i%5 == 0 and i%3 != 0:
        summ += i
    elif i%3 == 0 and i%5 == 0:
        summ += i
print(summ)