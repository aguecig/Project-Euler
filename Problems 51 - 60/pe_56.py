values = []
summ = 0

for i in range(1,100):
	for j in range(1,100):
		if i**j in values:
			continue
		else:
			values.append(i**j)

for k in range(len(values)):
	s = str(values[k])
	temp = 0
	for r in range(len(s)):
		temp = temp + int(s[r])
	if temp > summ:
		summ = temp

print(summ)
		
