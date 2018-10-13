
# 2. Given array of positive integers. 
# Return if subarray can add up to some N. True or false
def sum(nums, target):
	if len(nums) == 0:
		return False 
	elif len(nums) == 1:
		if nums[0] == target:
			return True
		else:
			return False
	
	if nums[0] == target or nums[1] == target:
		return True

	lo = 0
	hi = 1
	curr_sum = nums[lo] + nums[hi]
	while hi < len(nums):
		if curr_sum == target:
			return True
		elif curr_sum < target:
			hi = hi+1
			if hi < len(nums):
				curr_sum += nums[hi]
		else:
			curr_sum = curr_sum - nums[lo]
			lo += 1
	return False



nums = [3,3,2]
target  = 5
print(sum(nums, target))

