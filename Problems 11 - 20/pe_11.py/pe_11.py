# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:24:15 2019

@author: aguec
"""

def product():
    matrix = {}
    array = open('pe_11.txt','r')
    i = 0
    for line in array:
        matrix[i] = line
        i = i + 1
    
    mn = []
    for i in range(20):
        row = []
        for j in range(0,20):
            row.append(int(matrix[i][3*j] + matrix[i][3*j+1]))
        mn.append(row)

    # row test
    
    product = 0
    
    for r in range(20):
        for s in range(17):
            test = mn[r][s]*mn[r][s+1]*mn[r][s+2]*mn[r][s+3]
            if test > product:
                product = test
    
    # column test
    
    for u in range(20):
        for v in range(17):
            test = mn[v][u]*mn[v+1][u]*mn[v+2][u]*mn[v+3][u]
            if test > product:
                product = test    
    # forward diagonal test
    
    for a in range(17):
        for b in range(17):
            test = mn[a][b]*mn[a+1][b+1]*mn[a+2][b+2]*mn[a+3][b+3]
            if test > product:
                product = test
    
    # backward diagonal test
    'Originally when I had coded this problem, I had not considered the '
    'possibility of the backward diagonal (which is where the max sum lies)'
    'hence I was not obtaining the correct value!'
    ' GC 02/01/2019 '
    
    for e in range(17):
        for f in range(17):
            test = mn[19-e][f]*mn[18-e][f+1]*mn[17-e][f+2]*mn[16-e][f+3]
            if test > product:
                product = test
    print(product)