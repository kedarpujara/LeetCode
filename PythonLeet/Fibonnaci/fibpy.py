def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        print(lst)
        return lst
#print(fib(10))

def fib(n, m):
    if n == 0:
        return [0]
    elif n == 1:
        return [0,1]
    else:
        lst = fib(n-1, m)
        curr = lst[-1] + lst[-2]        
        if curr >= m:
            return lst 
        else:
            lst.append(curr)
print(fib(10, 100))