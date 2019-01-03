# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:10:27 2019

@author: aguec
"""

def collatz(n):
    
    #initialize sequence with x = 2
    sequence = [2,1]
    
    for i in range(1,n):
        if (i in sequence) == True:
            pass # if i is in the previous sequence, it will just be a shorter version of it.
        elif (i in sequence) == False:
            test = [i]
            a = i
            while a != 1:
                if a%2 == 0:
                    a = a/2
                    test.append(a)
                else:
                    a = 3*a + 1
                    test.append(a)
            if len(test) > len(sequence):
                sequence = test
    print(sequence[0])