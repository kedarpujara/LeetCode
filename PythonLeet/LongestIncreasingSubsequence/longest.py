class Solution(object):
    # def lengthOfLIS(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if len(nums) == 0:
    #         return None
    #     elif len(nums) == 1:
    #         return 1
    #     temp = 0
    #     max_length = 1
    #     curr_length = 1
    #     for i in range(1,len(nums)):
    #         temp = i
    #         while nums[temp] > nums[temp-1]:
    #             curr_length += 1
    #         max_length = max(max_length, curr_length)
    #         curr_length = 1
    #     return max_length


    def longest(self, nums):
        r = [-1 for i in range(len(nums))]
        t = [0 for i in range(len(nums))]

        length = 0
        for i in range(1, len(nums)):
            if nums[t[0]] > nums[i]:
                t[0] = i 
            elif nums[t[length]] < nums[i]:
                length += 1
                t[length] = i 
                r[t[length]] = t[length-1]
            else:
                index = self.ceil_index(nums, t, length, nums[i])
                t[index] = i 
                r[t[index]] = t[index-1]
        index = t[length]
        res = []
        while index != -1:
            res.insert(0, nums[index])
            index = r[index]
        
        return res

    def ceil_index(self, nums, t, end, s):
        start = 0
        length = end 
        while start <= end:
            mid = (start + end)/2
            if mid < length and nums[t[mid]] < s and s <= nums[t[mid+1]]:
                return mid+1
            elif nums[t[mid]] < s:
                start = mid+1
            else:
                end = mid-1
        return -1

def main():
    s = Solution()
    #nums = [10,9,2,5,3,7,101,102]
    nums = [3,4,-1,5,8,2,3,12,7,9,10]
    print(s.longest(nums))

main()