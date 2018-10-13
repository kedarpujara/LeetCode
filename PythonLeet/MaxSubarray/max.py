def max(nums):
	if len(nums) == 0:
		return 0
	elif len(nums) == 1:
		return nums[0]

	max_num = nums[0]
	dp = [0 for x in range(len(nums))]
	dp[0] = nums[0]

	for i in range(1,len(nums)):
		# if nums[i] + dp[i-1] < nums[i]:
		if dp[i-1] < 0:
			dp[i] = nums[i]
		else:
			dp[i] = nums[i] + dp[i-1]
		if dp[i] > max_num:
			max_num = dp[i]
	return max_num


nums = [-2, 3, -1, -4 , 4, 3, 1, 2 ,3 , -4, 1]
#nums = [-1,-2]
print(max(nums))