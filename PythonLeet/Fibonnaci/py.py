
def f(n, max):
    a, b = 0, 1
    total_sum = 0
    for i in range(0, n):
        a, b = b, a + b
        print(a)
        if a < max and a %2 == 0:
            total_sum += a 
        elif a >= max:
            break
            
    return total_sum

print(f(100, 100))