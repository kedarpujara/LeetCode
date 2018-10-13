
def product_array(nums):    
    temp = [1]*len(nums)
    #print(temp)    
    for i in range(1,len(nums)):
        temp[i] = temp[i-1]*nums[i-1]
    nums.append(1)
    curr = 1

    for i in range(len(temp)-1, -1, -1):        
        curr *= nums[i+1]
        temp[i] = temp[i]*curr
        
    print(temp)        
    return temp



nums = [1,2,3,4,5]
print(product_array(nums))