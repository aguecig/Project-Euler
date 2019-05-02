# -*- coding: utf-8 -*-
"""
Created on Wed Jan 02 15:11:47 2019

@author: aguec
"""

def palindrome():
    
    numbers = []
    for i in range(100,1000):  #can adjust the range of numbers here. Example,
        numbers.append(i)      #four digit numbers would have a range of 
    palindromes = []           #1000 to 10000
    for j in range(len(numbers)):
        for k in range(j,len(numbers)):
            test = str(numbers[j]*numbers[k])
            pal = True
            for r in range(len(test)):
                if test[r] != test[len(test)-1 - r]:
                    pal = False
                    
            if pal == True:
                palindromes.append(test)
                    
    int_pal = []
    for s in range(len(palindromes)):
        int_pal.append(int(palindromes[s]))
        
    print(max(int_pal))