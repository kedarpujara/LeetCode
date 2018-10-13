def isPrime(num):
	i = 2
	while i*i <= num:
		if num % i == 0:
			return False
		else:
			i += 1
	return True


print(isPrime(35))



def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))

