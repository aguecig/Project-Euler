# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:33:33 2019

@author: aguec
"""

def fact(n):
    result_set = set()
    for i in range(1, 1+int(n**0.5)):
        if n % i == 0:
            result_set.add(n // i)
            result_set.add(i)
    return len(result_set)
    
def tri_factors():
    count = 0
    for i in range(1,1000000):
        tri_num = i*(i+1)/2
        if(i%2 == 0):
            count = fact(i/2)*fact(i+1)
        elif(i%2 !=0):
            count = fact(i)*(fact((i+1)/2))
        if count >= 501:
            break
    print(tri_num)