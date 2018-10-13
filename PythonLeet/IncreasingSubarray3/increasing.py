def increase(a):
	i = 1
	counter = 0
	while i < len(a):
		if a[i] > a[i-1]:
			counter += 1
		else:
			counter = 0
		if counter == 2:
			return True
		i += 1
	return False

def increase_no_counter(a):
	if len(a) < 3:
		return False
	i = 2
	while i < len(a):
		if a[i] > a[i-1] and a[i] > a[i-2]:
			return True
		else:
			i += 1
	return False

a = [6,4,3,3,4,5]
print(increase_no_counter(a))
