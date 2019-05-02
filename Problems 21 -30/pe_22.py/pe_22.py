# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:52:21 2019

@author: aguec
"""

# sorting the names in a list to make manipulation more convenient

name_file = open('names.txt','r')
i = 0
name_list = []
for line in name_file:
    while i < len(line)-1:
        name = ''
        if line[i] != chr(34):
            i = i + 1
        elif line[i] == chr(34):
            j = i + 1
            while line[j] != chr(34):
                name = name + line[j]
                j = j + 1
        name_list.append(name)
        i = j + 2

#print(len(name_list)) #result shows 5163 names
        
ad = {chr(i):i-64 for i in range(65,65+26)}  #creating score dictionary for letters

alpha_names = sorted(name_list) # sorting names in alphabetical order

total_score = 0
for k in range(len(alpha_names)):
    score = 0
    for r in range(len(alpha_names[k])):
        score = score + ad[alpha_names[k][r]]
    score = score*(k+1)
    total_score = total_score + score

print(total_score)