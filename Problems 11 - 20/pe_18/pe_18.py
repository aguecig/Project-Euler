# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 17:46:48 2019

@author: aguec
"""

triangle_file = open('pe_18.txt','r')

triangle = {}
i = 0
for line in triangle_file:
    triangle[i] = line
    i = i + 1
    
tri = [['75']]
for k in range(1,len(triangle)):
    row = []
    for r in range(k+1):
        row.append(triangle[k][3*r:3*r+2])
    tri.append(row)
    
n = len(tri)
summ = []

for r in range(n-1):   #initializing the summ of the bottom two rows
    if int(tri[n-1][r]) > int(tri[n-1][r+1]):
        summ.append(int(tri[n-1][r]) + int(tri[n-2][r]))
    else:
        summ.append(int(tri[n-1][r+1]) + int(tri[n-2][r]))

for s in range(13):   #use bottom up approach. A top down approach will generally
    a = []            #not work (see: Greedy Algorithm)
    for t in range(len(summ)-1): 
        if summ[t] > summ[t+1]:
            a.append(summ[t] + int(tri[12-s][t]))
        else:
            a.append(summ[t+1] + int(tri[12-s][t]))
    summ = a

print('The largest sum is ',summ[0])
    
        