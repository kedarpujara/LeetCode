def threesome(ar):
	if len(ar) < 3:
		return False
	ar.sort()
	print(ar)
	if ar[0] > 0:
		return False

	lo = 0
	mid_lo = 1
	mid_hi = len(ar)-2
	hi = len(ar)-1
	print(ar[hi])
	solution = []
	curr = []
	while mid_lo < hi:
		print(lo)
		print(mid_lo)
		print(hi)
		print("")

		if (ar[lo] + ar[mid_lo] + ar[hi]) < 0:
			lo += 1
			mid_lo += 1
		elif (ar[lo] + ar[mid_lo] + ar[hi]) > 0: 
			hi -= 1 
		else:
			print("here")
			print(abs(ar[lo]) + abs(ar[mid_lo]))
			print(ar[lo])
			print(ar[mid_lo])
			print(ar[hi])
			print("")
			print("")
			curr.append(ar[lo])
			curr.append(ar[mid_lo])
			curr.append(ar[hi])
			solution.append(curr)
			curr = []
			lo += 1
			mid_lo += 1

	# lo = 0
	# mid_lo = 1
	# mid_hi = len(ar)-2
	# hi = len(ar)-1

	# while lo <= hi:
	# 	print(lo)
	# 	print(hi)
	# 	if (abs(ar[lo]) > abs(ar[mid_hi])) + abs(hi):
	# 		lo += 1
	# 	elif (abs(ar[lo] < abs(ar[mid_hi])) + abs(hi)):
	# 		hi -= 1
	# 		mid_hi -= 1 
	# 	elif (abs(ar[lo] == abs(ar[mid_hi])) + abs(hi)):
	# 		curr.append(ar[lo])
	# 		curr.append(ar[mid_hi])
	# 		curr.append(ar[hi])
	# 		solution.append(curr)

	return solution


ar = [0,5,7,-6, -4, -3,8,-2]
print(threesome(ar))
