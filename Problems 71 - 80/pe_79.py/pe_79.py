# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:39:56 2019

@author: aguec
"""

logins = open('keylog.txt','r')

chars = []

for line in logins:
    chars.append(int(line))
    
# a quick glance at the different logins shows that there is no 
# 4 or 5 in the passcode. 
    
starters = []
enders = []
mids = []

for i in range(len(chars)):
    if str(chars[i])[0] in starters:
        continue
    else:
        starters.append(str(chars[i])[0])

# from this we can see that the passcode cannot start with a 9 or a 0.
        
for i in range(len(chars)):
    if str(chars[i])[2] in enders:
        continue
    else:
        enders.append(str(chars[i])[2])

# from this we can see the passcode cannot end with a 3 or 7
        
for i in range(len(chars)):
    if str(chars[i])[1] in mids:
        continue
    else:
        mids.append(str(chars[i])[1])

# and from this, we can see that 0 and 7 never show up in the middle.
        
# putting this together, the passcode must begin with 7 and end in 0.
'7 _ _ _ _ _ _ _ 0 '
        
# now just piece the rest together by looking at the text file:
        
'73162890'

logins.close()