# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:52:41 2019

@author: aguec
"""

numbers = [0]
for i in range(1,1000000):
    numbers.append(i)
    
decimal = ''

for j in range(len(numbers)):
    decimal = decimal + str(numbers[j])


d = int(decimal[1])*int(decimal[10])*int(decimal[100])*int(decimal[1000])*int(decimal[10000])*int(decimal[100000])*int(decimal[1000000])

print(d)