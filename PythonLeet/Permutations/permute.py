def permute(nums):
	res = []
	permuteHelper(res, nums,[])
	return res


def permuteHelper(res,nums,curr):
	print(curr)
	print(nums)
	# print(res)
	print("")
	if len(nums) == 0:
		res.append(curr[:])
		#print(res)

	else:
		for i in range(len(nums)):
			num = nums[i]
			curr.append(num)
			nums.pop(i)
			permuteHelper(res,nums,curr)
			nums.insert(i,num)
			curr.pop()


nums = [1,2,3]
print(permute(nums))
