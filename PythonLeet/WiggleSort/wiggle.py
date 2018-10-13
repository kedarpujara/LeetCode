class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []        
        i = 0
        while i < len(nums):            
            #Even cases 
            if i%2 == 0:                
                if (i+1) < len(nums) and (i-1)>0:
                    while nums[i] >= nums[i-1] or nums[i] >= nums[i+1]:                  
                        if nums[i] > nums[i+1]:                        
                            self.swap(nums,i,i+1)                        
                        elif nums[i] == nums[i+1]:
                            if i+2 < len(nums):
                                self.swap(nums,i+1,i+2)
                            else:
                                break
            #Odd cases 
            else:
                if (i+1) < len(nums):
                    while nums[i] <= nums[i-1] or nums[i] <= nums[i+1]:
                        if nums[i] < nums[i+1]:
                            self.swap(nums,i,i+1)
                        elif nums[i] == nums[i+1]:
                            if (i+2) < len(nums):
                                self.swap(nums,i+1, i+2)
                            else:
                                break    
            i += 1
        return nums

    
    
    def swap(self, nums,i,j):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp

                        
def main():
    s = Solution()
    nums =[1,5,1,1,6,4]
    print(s.wiggleSort(nums))

main()
