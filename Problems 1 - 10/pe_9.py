# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 11:05:14 2019

@author: aguec
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:11:47 2018

@author: aguec
"""
import math
def triples():
    
    squares = []
    
    for i in range(1,501):
        squares.append(i**2)
    
    a = []
    for j in range(1,501):
        a.append(j)
    b = a
    
    c = 0

    for r in range(len(a)):
        for s in range(len(b)):
            c = math.sqrt(a[r]**2 + b[s]**2)
            if c%1 == 0:
                if a[r] + b[s] + int(c) == 1000:
                    return (a[r],b[s],c, a[r]*b[s]*c)
                else:
                    pass