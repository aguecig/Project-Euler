# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:05:20 2019

@author: aguec
"""

words = open('p059_cipher.txt','r')

'first, we transfer the ciphertext entries to a list'
temp = ''
letters = []
for i in words:
    for j in range(3203):
        if i[j] == ',':
            letters.append(int(temp))
            temp = ''
        else:
            temp = temp + i[j]
letters.append(73) #i had trouble getting the last character in the list xP 

test = [q for q in range(97,123)]
test.append(32)  #include the SPACE character ! it significantly adds to the totals.

'because we are told that the key is 3 characters long, we break the ciphertext'
'up into 3 blocks'
first = []
second = []
third = []

for x in range(0,len(letters),3):
    first.append(letters[x])
    if x > len(letters) - 2:
        break
    second.append(letters[x+1])
    third.append(letters[x+2])

#print(len(first))
#print(len(second))
#print(len(third))

total_count_first = []
total_count_second = []
total_count_third = []

'now we make a list for each block that keeps track of how many times a lower'
'case letter maps the cipher text into an alphabet symbol or the space symbol'
' so for example, if the lower case letter chosen for the potential key mapped'
' a ciphertext entry to the ascii character &, we know this isnt a possible key'
' and so the total count will be lower'
for r in range(97,123):
    message = ''
    count = 0
    for s in range(0,len(first)):
        message = message + chr(r^first[s])
        if int(r^first[s]) in test:
            count = count + 1
    total_count_first.append(count)

for r1 in range(97,123):
    message = ''
    count = 0
    for s1 in range(0,len(second)):
        message = message + chr(r1^second[s1])
        if int(r1^second[s1]) in test:
            count = count + 1
    total_count_second.append(count)
    
for r2 in range(97,123):
    message = ''
    count = 0
    for s2 in range(0,len(third)):
        message = message + chr(r^third[s2])
        if int(r2^third[s2]) in test:
            count = count + 1
    total_count_third.append(count)

'the print commands below will show you which letter is the key for the first,'
'second, and third letters of the password based on xors mapping to the english'
'alphabet, or space character.'
#print(total_count_first)
#print(total_count_second)
#print(total_count_third)

'now we have found that the key is likely to be "god", so we decrypt with it'
decrypt = []
for T in range(0,len(letters),3):
    decrypt.append(chr(103^letters[T]))
    if T > len(letters) - 2 :
        break
    decrypt.append(chr(111^letters[T+1]))
    decrypt.append(chr(100^letters[T+2]))

final_message = ''
for D in range(len(decrypt)):
    final_message = final_message + decrypt[D]

print(final_message)

ascii_dict = {chr(D):D for D in range(0,256)}

'for project euler problem 59, we are required to produce an ASCII score for'
'the plain text'
score = 0
for S in range(len(final_message)):
    score = score + ascii_dict[final_message[S]]

print(' ')
print('ASCII score is', score)