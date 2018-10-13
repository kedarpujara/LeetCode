class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return 1
        temp = 0
        max_length = 1
        curr_length = 1
        for i in range(1,len(nums)):
            temp = i
            while nums[temp] > nums[temp-1]:
                curr_length += 1
            max_length = max(max_length, curr_length)
            curr_length = 1
        return max_length

def main():
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums))

main()