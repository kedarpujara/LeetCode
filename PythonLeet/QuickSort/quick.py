def divide(a, start, end):
	if start >= end:
		return
	print(a)

	pIndex = partition(a, start, end)
	divide(a,start,pIndex-1)
	divide(a,pIndex+1,end)
	return a

def partition(a, start, end):
	pivot = a[end]
	pIndex = i = start

	while i <= end:
		if a[i] <= pivot:
			a[pIndex],a[i] = a[i], a[pIndex]
			pIndex += 1
		i += 1
	return pIndex-1

#ar = [2,4,1,6,8,5,3,7]
ar = [7,2,1,6,8,5,3,4]
start = 0
end = len(ar)-1
print(divide(ar,start,end))