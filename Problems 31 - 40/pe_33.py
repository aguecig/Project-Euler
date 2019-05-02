# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:20:56 2019

@author: aguec
"""

from fractions import Fraction

candidates = []

for i in range(10,100):
    if str(i)[1] == '0':
        continue
    for j in range(i+1,100):
        if str(j)[1] == '0':
            continue
        f = Fraction(i,j)
        if str(i)[0] == str(j)[0] and float(int(str(i)[1])/int(str(j)[1])) == float(f):
            candidates.append([i,j])
        if str(i)[0] == str(j)[1] and float(int(str(i)[1])/int(str(j)[0])) == float(f):
            candidates.append([i,j])
        if str(i)[1] == str(j)[0] and float(int(str(i)[0])/int(str(j)[1])) == float(f):
            candidates.append([i,j])
        if str(i)[1] == str(j)[1] and float(int(str(i)[0])/int(str(j)[0])) == float(f):
            candidates.append([i,j])
        else:
            pass
print(candidates)

product = 1

for r in range(len(candidates)):
    product = product*Fraction(candidates[r][0],candidates[r][1])
    
print(product)