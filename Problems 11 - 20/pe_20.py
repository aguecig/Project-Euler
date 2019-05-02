# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 09:34:39 2019

@author: aguec
"""

import math

x = str(math.factorial(100))
summ = 0
for i in range(len(x)):
    summ = summ + int(x[i])

print(summ)