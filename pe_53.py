import math

count = 0
for n in range(23,101):
	for r in range(2,n):
		nCr = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
		if nCr > 1000000:
			count = count + 1

print(count)
