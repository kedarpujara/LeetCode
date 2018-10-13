import collections
import heapq
def top_k(nums,k):
	c = collections.Counter(nums)
	print(c)

	h = []
	heapq.heapify(h)
	print h

	for key, val in c.items():
		heapq.heappush(h,(-val,key))

	#print h
	solution = []

	for i in range(k):
		val,key = heapq.heappop(h)
		solution.append(key)
	print solution
	return solution











nums = [1,1,1,2,3,3]
k = 2
top_k(nums,k)