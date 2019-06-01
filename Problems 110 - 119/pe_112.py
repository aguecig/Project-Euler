# -*- coding: utf-8 -*-
"""
Created on Fri May 31 23:43:08 2019

@author: aguec
"""

import timeit
start = timeit.default_timer()
# The numbers 1 through 99 cannot be bouncy, so we start at 100
number = 100
ratio = 0
bouncy_numbers = 0

while ratio != 0.99:
    test = ''
    bouncy = False
    # we want to compare the digits in the number, so we construct a list of 
    # the digits
    digits = list(str(number))
    # first we check to see if all the digits are the same number, in which 
    # case the number cannot be bouncy
    if len(set(str(number))) == 1:
        number += 1
        continue
    else:
        # now we pass through the first i - 1 digits that are the same value
        first_digit = digits[0]
        for i in range(1,len(digits)):
            if digits[i] == first_digit:
                continue
            else:
                new_digit_index = i
                break
        # if all digits but the last digit are the same value, the number still 
        # cannot be bouncy        
        if i == len(digits) - 1:
            number += 1
            continue
        # if the first digit to be different is greater than the first digit, 
        # we now test the rest of the digits to see if they are all in an 
        # increasing order
        elif int(digits[i]) > int(first_digit):
            test = 'increasing'
        # in the opposite case, the test will check decreasing order
        else:
            test = 'decreasing'
        # preform the tests
        if test == 'increasing':
            for j in range(i,len(digits)-1):
                if int(digits[j+1]) >= int(digits[j]):
                    continue
                else:
                    bouncy = True
                    break
        elif test == 'decreasing':
            for j in range(i,len(digits)-1):
                if int(digits[j+1]) <= int(digits[j]):
                    continue
                else:
                    bouncy = True
                    break
    # add to the total bouncy numbers if the test failed, and update the raio
    # then proceed to the next number if the ratio is not 99%
    if bouncy == True:
        bouncy_numbers += 1
        ratio = bouncy_numbers/number
        number += 1
        continue
    # otherwise, proceed to the next number
    else:
        number += 1
        continue
    
print(number - 1)
end = timeit.default_timer()
print('runtime:',end-start,'seconds')