def count(a):
	temp = 0
	duplicates = []
	missing = []
	i = 0
	while i < len(a):
		if a[i] != (i+1):
			temp = a[i]
			if a[i] != a[temp-1]:
				a[i] = a[temp-1]
				a[temp-1] = temp
			else:
				duplicates.append(a[i])
				missing.append(i+1)
				i += 1
		else:
			i += 1
	print duplicates
	print missing
	return a



ar = [3,6,8,7,2,2,1,7]
ar2 = [1,1]
print(count(ar2))