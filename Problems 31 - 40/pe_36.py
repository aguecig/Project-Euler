# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 23:53:50 2019

@author: aguec
"""

# program checks to see if (for all integers less than n) if its integer and 
# binary representation are palindromes. The sum of all such integers less than
# n is then computed.
# note: leading zeros do not count in this sum.

def palindrome(n):
    
    palindromes = []
    
    for i in range(n):
        num = str(i)
        if num[len(num)-1] == 0:
            continue
        else:
            pal = True
            for j in range(len(num)):
                if num[j] != num[len(num) - 1 - j]:
                    pal = False
                    break
                else:
                    num_bin = bin(i)
                    num_bin = num_bin[2:len(num_bin)]
                    for k in range(len(num_bin)):
                        if num_bin[k] != num_bin[len(num_bin) - 1 - k]:
                            pal = False
                            break
            if pal == True:
                palindromes.append(i)
    
    print(sum(palindromes))