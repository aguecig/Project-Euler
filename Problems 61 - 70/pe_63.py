pdc = []
count = 0
for e in range(1,100): # keep adjusting this range until count stalls
	n = 1          # since eventually, the powers will get too big
	while len(str(n**e)) < e + 1:
		if len(str(n**e)) == e:
			count = count + 1
			pdc.append(n**e) # not neccessary for the challenge,
		n = n + 1                # but interesting to see the numbers
print(count)
print(pdc)
