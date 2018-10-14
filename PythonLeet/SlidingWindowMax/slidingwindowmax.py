from collections import deque 
class SlidingWindow:
    def sliding(self, nums, k):
        if not nums:
            return []
        res = []
        for i in range(k-1, len(nums)):
            curr_window = nums[i-k+1:i+1]
            print(curr_window)
            res.append(max(curr_window))
            print(res)
            print("")
        return res 

    def sliding_alternate_1(self, nums, k):
        temp_start = -1
        res = []
        for i in range(k-1, len(nums)):
            temp_start += 1
            j = temp_start
            curr_max = nums[j]
            while j <= i:
                curr_max = max(curr_max, nums[j])
                j += 1
            res.append(curr_max)
        return res 

    def sliding_queue(self, nums, k):
        res = []
        q = deque()
        ri = 0
        for i in range(len(nums)):
            while q and q[0] < (i - k + 1):
                q.pop()

            while q and q[-1] < nums[i]:
                q.popleft()

            q.appendleft(i)

            if i >= k-1:
                ri += 1
                res.append(nums[q[0]])
        return res 


def main():
    sw = SlidingWindow()
    nums = [-1,5,3,5,6,-7,1,2,3,2,1]
    k = 3
    #print(sw.sliding(nums, k))
    #sw.sliding_alternate_1(nums, k)
    print(sw.sliding_queue(nums, k))


main()