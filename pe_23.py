# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 18:07:25 2019

@author: aguec
"""

# upper limit: By mathematical analysis, it can be shown that all integers 
# greater than 28123 can be written as the sum of two abundant numbers
# so our upper limit is 28123 for this particular problem.

abundant = []

for i in range(12,28124): #finding all abundant numbers below 28124
    summ = 0
    for j in range(1,int(i/2) + 1):
        if i%j == 0:
            summ = summ + j
    if summ > i:
        abundant.append(i)
        
# the idea now is to open a list of length 28124 all of entries equivalent to 0.
# we check the sum of all abundant numbers, and if the sum is less than 28124,
# we replace the 0 in the list with the number to indicate that it can in fact 
# be written as the sum of two abundant numbers.        

sums = [0]*28124
for r in range (0, len(abundant)):
    for s in range (r, len(abundant)):
            sum_abundant = abundant[r]+abundant[s]
            if (sum_abundant<= 28123):
                if (sums[sum_abundant] == 0):
                    sums[sum_abundant] = sum_abundant

# now, we just sum up the indicie values in the list that have entries zero, for
# they are the numbers that cannot be expressed as the sum of two abundant numbers.

total = 0
for t in range (1,len(sums)):
    if sums[t] == 0:
        total = total + t

print(total)