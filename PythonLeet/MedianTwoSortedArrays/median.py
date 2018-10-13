def findMedianSortedArrays(nums1, nums2):
	
	comb = combinedArray(nums1, nums2)
	length = len(comb)

	print(comb)
	print(length/2-1)
	isOdd = False
	if length % 2 == 1:
		isOdd = True
	if isOdd:
		return comb[length/2]
	else:
		return (float(comb[length/2] + comb[length/2 -1])/float(2))



def combinedArray(nums1, nums2):
	p1 = 0
	p2 = 0
	ar = []

	while p1 < len(nums1) and p2 < len(nums2):
		if p1 < len(nums1) and p2 < len(nums2):
			if nums1[p1] < nums2[p2]:
				ar.append(nums1[p1])
				p1 += 1
			else:
				ar.append(nums2[p2])
				p2 += 1
	if p1 < len(nums1):
		for i in range(p1,len(nums1)):
			ar.append(nums1[i])

	elif p2 < len(nums2):
		for i in range(p2, len(nums2)):
			ar.append(nums2[i])

	return ar

print findMedianSortedArrays([1,2,6,8,9], [3,4,5])