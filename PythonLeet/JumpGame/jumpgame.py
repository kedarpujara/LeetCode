class Stack:
     def __init__(self):
         self.items = []

     # I have changed method name isEmpty to is_empty
     # because in your code you have used is_empty
     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
def jumpgame(nums):
	if not nums:
		return False

	i,j,length = 0,0,len(nums)-1

	while j <= length:
		#print(i)
		print(j)
		if nums[j] == 0:
			return False
		curr_val = nums[j]
		print(curr_val)
		j += curr_val
		if j >= length:
			return True
		while nums[j] == 0 and j > i:
			j -= 1
		print(j)
		print("hello")
		i += 1

	return False

def jump(nums):
	if not nums:
		return False
	if len(nums) == 1:
		return True
	s = Stack()
	s.push(nums[0])
	i = 1
	curr_pos = 0
	length = len(nums) - 1
	while s.isEmpty() == False:
		curr = s.pop()
		#curr_pos += curr
		
		for j in range(i,curr+i):
			print(j)
			if j == length:
				return True
			s.push(nums[j])
		i += curr
	return False

	 


nums = [3,1,4,0,1,2]
nums2 = [3,2,1,0,4]
nums3 = [2,5,0,0]
nums4 = [3,0,8,2,0,0,1]
print(jump(nums2))
