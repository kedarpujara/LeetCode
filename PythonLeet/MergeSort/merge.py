def merge(ar,lo,hi):
	if len(ar) == 1:
		if ar[lo]
	mid = (hi + lo)/2
	l = merge(lo,mid)
	r = merge(mid+1,high)


def mergeSort(ar):
	lo = 0
	hi = len(ar)-1
	mid = len(ar)/2
	left = merge(ar, lo, mid)
	right = merge(ar, mid+1, hi)
	
	k = 0
	while i < len(left) or j < len(right):
		if i < len(left) and j < len(right):
			if left[i] <= right[j]:
				ar[k] = left[i]
				i += 1
				k += 1
			else:
				ar[k] = right[j]
				j += 1
				k += 1

		elif i < len(left):
			ar[k] = left[i]
			i += 1
			k += 1
		else:
			ar[k] = right[j]
			j += 1
			k += 1
	return sorted_ar

ar = [2,4,1,6,8,5,3,7]

print(mergeSort(ar))
