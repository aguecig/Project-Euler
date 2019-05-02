# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 22:17:08 2019

@author: aguec
"""

# I would just like to note that I obtained the correct output on my first
# run of this program, and that is quit an achievement for me.

import timeit

start = timeit.default_timer()

non_lychrel = []
count = 0

for i in range(1,10000):
    if i in non_lychrel:
        continue
    temp = []
    a = i
    s = str(a)
    b = int(s[::-1])
    for j in range(49):
        temp.append(a)
        temp.append(b)
        test = str(a + b)
        if len(test) %2 == 0:    # case when number of digits is even
            first_half = test[0:int(len(test)/2)]
            second_half = test[int(len(test)/2):len(test)]
            second_half = second_half[::-1]
        elif len(test) %2 != 0:  # case when number of digits is odd
            first_half = test[0:int(len(test)/2) + 1]
            second_half = test[int(len(test)/2): len(test)]
            second_half = second_half[::-1]
        if first_half == second_half:  # check to see if palindrome
            for k in range(len(temp)):
                non_lychrel.append(temp[k])
            break
        elif j != 48:
            a = int(test)
            b = int(test[::-1])
            continue
        elif j == 48:
            count = count + 1
            
print('The number of lychrel numbers from 1 to 10000 is: ' , count)

end = timeit.default_timer()

print('Runtime: ', end - start, ' seconds')