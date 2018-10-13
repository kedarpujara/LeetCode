#import Math
def max_product(nums):
    neg_indices = []
    max_product = 0
    for i in range(len(nums)):
        if nums[i] < 0:            
            neg_indices.append(i)
    print(neg_indices)

    if len(neg_indices) % 2 == 0:
        return product(nums,0,len(nums)-1)

    else:
        for i in range(len(neg_indices)):
            max_product = max(max_product, product(nums, 0,neg_indices[i]-1), product(nums,neg_indices[i]+1, len(nums)-1))
    return max_product

def product(nums,i,j):
    product = 1
    while i <= j:
        product *= nums[i]
        i += 1
    return product

#nums = [2,3,-2,4]
nums2 = [-2,0,-1]
print(max_product(nums2))
