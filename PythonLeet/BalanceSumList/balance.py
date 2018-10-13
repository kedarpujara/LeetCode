def balanced(a):
	total_sum = 0
	min_num_index = -1
	for i in range(len(a)):
		total_sum += a[i]
	
	left, right = 0, 0
	min_diff = 1390103847198324
	for i in range(len(a)):
		left += a[i]
		right = total_sum - left
		if abs(left-right) < min_diff:
			min_diff = abs(left-right)
			min_index = i
	print(min_diff)			
	return min_index


a = [16,5,22,11,8,10]
print(balanced(a))