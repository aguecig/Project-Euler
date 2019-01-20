# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:20:25 2019

@author: aguec
"""

words = open('words.txt','r')

i = 0
word_list = []
# put the words from the text file into a list
for line in words:
    while i < len(line)-1:
        word = ''
        if line[i] != chr(34):
            i = i + 1
        elif line[i] == chr(34):
            j = i + 1
            while line[j] != chr(34):
                word = word + line[j]
                j = j + 1
        word_list.append(word)
        i = j + 2
        
#print(word_list)

# define a score dictionary for letters A to Z (capitals)
alpha_dict = {chr(64+r):r for r in range(1,27)}

#print(alpha_dict)

scores = []

# score each word
for s in range(len(word_list)):
    score = 0
    for t in range(len(word_list[s])):
        score = score + alpha_dict[word_list[s][t]]
    scores.append(score)

# print(max(scores))  # this returned a value of 192. Use as upper bound for
                      # triangle number search.

tri_nums = []

# calculate triangle numbers to 192

tn = 0
n = 1
while tn < 193:
    tn = (1/2)*n*(n+1)
    tri_nums.append(tn)
    n = n + 1

tri_nums.pop()  #remove the last value which is greater than 192.

#print(tri_nums)

wtns = []  # wtns stands for word with triangle number scores
# finally, find which scores are triangle numbers.
for v in range(len(scores)):
    if scores[v] in tri_nums:
        wtns.append(scores[v])

#print(wtns)
print(len(wtns))