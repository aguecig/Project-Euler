mult = [1,2,3,4,5,6,7,8,9]
pandigitals = []

for i in range(1,10000):
	if len(str(i)) != len(set(str(i))):
		continue
	test = True
	candidate = ''
	for j in range(9):
		product = i*mult[j]
		candidate = candidate + str(product)
		if '0' in candidate:
			test = False
			break
		elif len(candidate) != len(set(candidate)):
			test = False
			break
		elif len(set(candidate)) == 9:
			test = True
			break
		else:
			continue
	if test == True:
		pandigitals.append(candidate)

print(pandigitals)
print(max(pandigitals))

# I would just like to make a note of this challenge. I recall attempting to solve it probably about a month ago, and I did spend quite a bit of time and effort on it, however I couldn't quite get the code right, and my alogirithm seemingly had a very large run time. Eventually, I gave up in what was probably frustrating knowing that I would one day return to it. Today I did finally return to it, and I solved the problem in less than 10 minutes, with a practically instantaneous run time. I think it is a key moment in my development of how I think about programming, and how far I have come in such a short period of time. It's important to realize things like this and for me to understand that I am capable of much when it comes to the way I think and solve problems.
#GC, Feb 21 2019 12:13 AM 
