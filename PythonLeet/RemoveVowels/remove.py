def remove(s):
	vowels = ['a','e','i','o','u']
	i = 0
	while i < len(s):
		if s[i] in vowels:
			s = s.replace(s[i],"")
		i += 1
	print s
	return s
remove("hellsafasdfasfo")

