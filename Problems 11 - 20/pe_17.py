# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:39:32 2019

@author: aguec
"""

digits = ['one','two','three','four','five','six','seven','eight','nine']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
a = 'and'

numbers = digits + teens

for i in tens:
    for j in digits:
        numbers.append(i+j)
for i in tens:
    numbers.append(i)
print(numbers)
        
prefix = []

for i in digits:
    prefix.append(i+'hundred'+a)

# number of characters in the first 99 numbers
f99l = sum([10*len(i) for i in numbers])

# number of characters in the 100 prefixes
hl = sum([99*len(i) for i in prefix])

# length of the hundred numbers and one thousand
specialcase = sum([len(i+'hundred') for i in digits])
specialcase += len('onethousand')

# total length calculation
print(f99l+hl+specialcase)