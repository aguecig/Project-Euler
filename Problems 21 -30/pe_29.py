# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:26:02 2019

@author: aguec
"""

power = []

for i in range(2,101):
    for j in range(2,101):
        if i**j in power:
            continue
        else:
            power.append(i**j)
            
print(len(power))