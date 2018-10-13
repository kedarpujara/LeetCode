def climb_stairs(n):
    num_ways = 0
    climb_helper(n,0,num_ways)
    return num_ways

def climb_helper(n, curr, num_ways):
    # if curr > n:
    #     return num_ways
    if curr >= n:
        return num_ways
    else:
        climb_helper(n, curr+1, num_ways+1)
        climb_helper(n,curr+2, num_ways+1)

def climbStairs3(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for i in xrange(2, n):
        tmp = b
        b = a+b
        a = tmp
        print(tmp)
        print(b)
        print("")
    return b



def fib_bottom_up(n):
    if n == 1:
        return 1
    






a = [1,2]
b = [4,5,7]
zupped = zip(a,b)
print(zupped)
print(climbStairs3(2))