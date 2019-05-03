# -*- coding: utf-8 -*-
"""
Created on Fri May  3 13:33:38 2019

@author: aguec
"""

f0 = 1
f1 = 2
summ = 2

while f1 < 4000000:
    temp = f1
    f1 = f0 + f1
    f0 = temp
    if f1 < 4000000 and f1%2 == 0:
        summ += f1

print(summ)