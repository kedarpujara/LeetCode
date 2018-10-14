def get_bigger(nums):
    left_sum, right_sum = 0, 0
    size = 1
    i = 1
    left = True 
    while i < len(nums):
        j = 0
        while j < size and i < len(nums):
            if left:
                if nums[i] != -1:
                    left_sum += nums[i]     
            else:
                if nums[i] != -1:
                    right_sum += nums[i]
            i += 1
            j += 1
        
        if left:
            left = False 
        else:
            left = True 
            size *= 2

    print(left_sum)
    print(right_sum)

nums = [9,20,16,3,-1,15,10]#,-1,2,-1,-1,-1,6,-1,-1]
get_bigger(nums)