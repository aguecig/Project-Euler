# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 23:32:19 2019

@author: aguec
"""

# the program finds circular primes up to an integer n.
# calls program 'prime_generator.py', so be sure to have it in the same directory.

def circular_primes(n):

    import prime_generator
    primes = prime_generator.primes(n)
    
    primes = primes[4:len(primes)] # we dont want to test the single digit primes.
    
    circle_primes = [2,3,5,7]
    
    for i in range(len(primes)):
        if '0' in str(primes[i]):
            continue
        elif '2' in str(primes[i]):
            continue
        elif '4' in str(primes[i]):
            continue
        elif '6' in str(primes[i]):
            continue
        elif '8' in str(primes[i]):
            continue
        else:
            primality = True
            L = list(str(primes[i]))
            for j in range(1,len(L)):
                L.append(L.pop(0))
                number = ''
                for k in range(len(L)):
                    number = number + L[k]
                if int(number) not in primes:
                    primality = False
                    break
            if primality == True:
                circle_primes.append(primes[i])
                 
    print(len(circle_primes))