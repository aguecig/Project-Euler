# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 21:00:49 2019

@author: aguec
"""

import itertools

lexico = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

m = lexico[999999]

millionth = ''
for i in range(len(m)):
    millionth = millionth + str(m[i])

print(millionth)