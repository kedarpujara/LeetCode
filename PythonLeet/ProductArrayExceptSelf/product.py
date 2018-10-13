def product(ar):
	res = [0 for i in range(len(ar))]
	res[0] = 1
	for i in range(1,len(ar)):
		res[i] = ar[i-1] * res[i-1]
	print(res)
	print(ar)
	for i in range(len(ar)-1,0,-1):
		print(i)
		res[i] *= res[0]
		res[0] *= ar[i]
	print(res)

product([1,2,3,4])