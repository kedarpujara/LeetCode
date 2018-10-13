class BST:
    def search(self, nums, target):
        if nums[0] < nums[len(nums)-1]:
            return self.binary_search(nums, target)

        first_val = nums[0]
        index = 0
        for i in range(1,len(nums)):            
            if nums[i] < nums[i-1]:
                pivot = i
                if target > first_val:
                    index = self.binary_search(nums[:i], target)
                else:
                    index = self.binary_search(nums[i:], target)   
                    index += i         
                break             
        return index 
                


    def binary_search(self, nums, target):
        mid = len(nums)/2
        print(mid)
        if len(nums) == 1:
            if target == nums[mid]:
                return mid
            else:
                return -1                
        print(mid)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.binary_search(nums[mid+1:], target)
        else:
            return self.binary_search(nums[:mid], target)




    def search_sorted_array(self, nums, start, end, target):        
        mid = start + (end-start)/2 

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            if target > nums[end]:
                return self.search_sorted_array(nums, start, mid-1, target)
            else:
                return self.search_sorted_array(nums, mid+1, end, target)
        #elif target < nums[mid]:
        else:
            if target > nums[start]:
                return self.search_sorted_array(nums, start, mid-1, target)
            elif target < nums[start]:
                return self.search_sorted_array(nums, mid+1, end, target)
        return -1



def main():
    b = BST()
    nums = [3,5,1]
    print(b.search_sorted_array(nums, 0, len(nums)-1, 3))
main()