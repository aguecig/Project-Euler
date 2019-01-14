# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 20:01:44 2019

@author: aguec
"""

# sample square for 7x7 (n = 3 in program, see explanation below)

#   43 44 45 46 47 48 49 
#   42 21 22 23 24 25 26 
#   41 20  7  8  9 10 27 
#   40 19  6  1  2 11 28 
#   39 18  5  4  3 12 29 
#   38 17 16 15 14 13 30 
#   37 36 35 34 33 32 31
    
'note for input: the value of n in the program gives the output for a square'
'that is in acuality 2n + 1 dimensional. So, to obtain the value for a square'
'of dimension 1001, we need to solve : '
' 2n + 1 = 1001'
' 2n = 1000 '
' n = 500'

def spiral_diagonals(n):
    
    summ = 1
    value = 1
    advance = 2
    
    for i in range(n):
        value = value + advance
        for j in range(4):
            summ = summ + value + j*advance
        value = value + advance*3
        advance = advance + 2
        
    
    print(summ)