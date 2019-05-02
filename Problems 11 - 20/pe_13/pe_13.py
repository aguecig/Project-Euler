# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:40:12 2019

@author: aguec
"""

number_file = open("pe_13.txt",'r')

summation = 0

for line in number_file:
    summation = summation + int(line)

summation = str(summation)

print(summation[0:10])