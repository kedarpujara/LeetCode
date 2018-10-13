import math
def min(nums):
	if len(nums) == 1:
		return nums[0]
	nums.sort(reverse=True)
	print(nums)
	num1 = 0
	num2 = 1
	place = 0
	carry = 0
	total_sum = 0
	curr_sum = 0
	while num2 < len(nums):
		curr_sum = nums[num1] + nums[num2] + carry
		if curr_sum > 9:
			carry = 1
			curr_sum = curr_sum - 10
		else:
			carry = 0
		print curr_sum
		total_sum += int(curr_sum * math.pow(10,place))
		
		place += 1
		num1 += 2
		num2 += 2
		curr_sum = 0
	if len(nums) % 2 == 1:
		curr_sum = nums[num1] + carry
		total_sum += int(curr_sum * math.pow(10,place))


	return total_sum





nums = [6, 8, 4, 5, 6, 6,1]
print(min(nums))
