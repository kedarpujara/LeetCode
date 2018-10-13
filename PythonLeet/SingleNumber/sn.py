def sn(ar):
    nums = {}
    for i in range(len(ar)):
        if i in nums:
            nums[i] = nums[i] + 1
        else:
            nums[i] = 1
    #return the index which has a key value of 1

def sn2(ar):
    for i in range(len(ar)):


def main():
    ar = [4,1,2,1,2]
    print(sn(ar))

main()
