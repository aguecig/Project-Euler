import math

def factdigitsum(x):
	summ = 0
	for j in range(len(x)):
		summ = summ + math.factorial(int(x[j]))
	return summ

tracker = []

# So after brute forcing the approach, I realized that the output
# was showing that none of the values included a 5, 6 or 8. I'm
# not sure why this is the case mathematically, but refining the
# code to skip these test values made the run time siginficantly
# faster. 

for i in range(1,1000001):
	if '5' in str(i) or '6' in str(i) or '8' in str(i):
		continue
	values = [i]
	test = True
	s = i
	count = 1
	while test == True:
		s = str(s)
		s = factdigitsum(s)
		if s in values:
			test = False
		else:
			values.append(s)
			count = count + 1
	if count == 60:
		tracker.append(i)

print(tracker)
print(len(tracker))
