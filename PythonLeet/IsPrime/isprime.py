import math
def isPrime(num):
	isp = False
	
	i = 2
	while (i*i <= num):
		if (num % i == 0):
			isp = False	
			print("false")
			return isp
		else:
			isp = True 
		i = i+1

	if isp == True:
		print("true")
	return isp

isPrime(47)