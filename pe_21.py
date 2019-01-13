# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 12:56:39 2019

@author: aguec
"""

from functools import reduce
def amicable_sum(n):
    
    # first we find all proper factors for all integers less than n
    factor_list = []
    for k in range(1,n):
        factors = []
        factors =  (set(reduce(list.__add__, ([i, k//i] for i in range(1, int(k**0.5) + 1) if k % i == 0))))
        factors = sorted(list(factors))
        factors.pop() # only including proper factors of n
        factor_list.append(factors)
        
    # now we sum all the factors of each integer less than n
    summs = []
    for j in range(len(factor_list)):
        summs.append(sum(factor_list[j]))
    summs.insert(0,0)
    
    amicable_numbers = []
    for r in range(1,len(summs)):
        if summs[r] < n:
            if summs[summs[r]] == summs[r]: # must remove the case where a number
                pass                        # is its own amicable number. example:
            elif summs[summs[r]] == r:      # 6 because 1 + 2 + 3 = 6. 28 is another example.
                amicable_numbers.append(r)
            else:
                pass
    print(sum(amicable_numbers))
