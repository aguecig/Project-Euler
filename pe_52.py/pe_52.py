def search(N):
	candidates = []
	for n in range(2,N+1):
		for i in range(int(10**(n-1)),int(10**(n-1)+6.7*10**(n-2))):
			if '5' not in str(i):
				continue
			else:
				s = set(str(i))
				test = True
				for k in range(2,7):
					if set(str(k*i)) != s:
						test = False
						break
				if test == True:
					candidates.append(i)
	print(candidates) 

