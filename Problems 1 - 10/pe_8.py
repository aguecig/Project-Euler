# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 10:48:29 2019

@author: aguec
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:11:47 2018

@author: aguec
"""

def product(n):
    
    start = 0
    end = 12
    products = []
    
    while end < 992:
        for i in range(start,end):
            P = int(n[start])*int(n[start+1])*int(n[start+2])*int(n[start+3])*int(n[start+4])*int(n[start+5])*int(n[start+6])*int(n[start+7])*int(n[start+8])*int(n[start+9])*int(n[start+10])*int(n[start+11])*int(n[end])
            products.append(P)
            start = start + 1
            end = end + 1
    print (max(products))
    
    