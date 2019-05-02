# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:04:31 2019

@author: aguec
"""

numbers = []
for n in range(10,200000):
    
    s = str(n)
    power_sum = 0
    
    for i in range(len(s)):
        power_sum = power_sum + int(s[i])**5
        
    if str(power_sum) == s:
        numbers.append(int(s))

print(numbers)
print(sum(numbers))