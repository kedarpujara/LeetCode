class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = 1
        
        min_len = len(nums)-1
        
        for num in nums:
            if num >= s:
                return 1
        
        while lo < len(nums):            
            if nums[lo:hi] >= s:
                curr_len = hi-lo
                min_len = min(min_len, curr_len)
                lo += 1
                hi = lo + 1
            else:
                hi += 1

            print(lo)
            print(hi)
            print("")
            
        return min_len

def main():
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
main()

                
                
            