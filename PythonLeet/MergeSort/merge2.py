def merge(l,r):
	i = j = 0
	result = []
	while i < len(l) and j < len(r):
		if l[i] < r[j]:
			result.append(l[i])
			i += 1
		else:
			result.append(r[j])
			j += 1
	result.extend(l[i:])
	result.extend(r[j:])
	# if i < len(l):
	# 	result.append(l[i:])
	# elif j < len(r):
	# 	result.append(r[j:])
	return result

def mergeSort(ar):
	if len(ar) <= 1:
		return ar
	
	mid = len(ar)//2
	
	left = mergeSort(ar[:mid])
	right = mergeSort(ar[mid:])

	print(left)
	print(right)
	print("")
	
	return merge(left, right)


ar = [2,4,1,6,8,5,3,7]

print(mergeSort(ar))