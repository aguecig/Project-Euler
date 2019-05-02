# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:23:29 2019

@author: aguec
"""

import timeit

start = timeit.default_timer()
#from numpy.polynomial import Polynomial as P
from numpy.polynomial.polynomial import polymul as M

" For this problem, I have taken the combinatorics approach"
" I have reduced the problem to solving the following equation:"
" x1 + 2*x2 + 5*x3 + 10*x4 + 20*x5 + 50*x6 + 100*x7 + 200*x8 = 200"
" With the following restrictions:"
" 0 <= x1 <= 200 "
" 0 <= x2 <= 100 "
" 0 <= x3 <= 40 "
" 0 <= x4 <= 20 "
" 0 <= x5 <= 10 "
" 0 <= x6 <= 4 "
" 0 <= x7 <= 2 "
" 0 <= x8 <= 1 "
" Now make a generating function for each variable based off the coefficients from "
" the equation and restrictions. Then we multiply these generating functions "
" together and find the coefficient to the power of 200, which will yield the number"
" of possible solutions"

"I came across this problem quite a long time ago, probably back in January of 2019."
"Originally, I had no idea how to do it."
" Now it is May 01 of 2019, and I have just completed my combinatorics course at "
" McMaster University. We learned about generating functions and how to solve problems"
" that are of this flavour. So realizing this and directly applying what I learned to"
" something outside of school is pretty cool! "

p1 = tuple([1 for i in range(201)])
p2 = tuple([1 if i%2 == 0 else 0 for i in range(201)])
p3 = tuple([1 if i%5 == 0 else 0 for i in range(201)])
p4 = tuple([1 if i%10 == 0 else 0 for i in range(201)])
p5 = tuple([1 if i%20 == 0 else 0 for i in range(201)])
p6 = tuple([1 if i%50 == 0 else 0 for i in range(201)])
p7 = tuple([1 if i%100 == 0 else 0 for i in range(201)])
p8 = tuple([1 if i%200 == 0 else 0 for i in range(201)])

mult = M(p1,p2)
poly = [p3,p4,p5,p6,p7,p8]

for j in range(len(poly)):
    mult = M(mult,poly[j])
    
print(mult[200])
finish = timeit.default_timer()

print('runtime = ',finish - start,' ms')