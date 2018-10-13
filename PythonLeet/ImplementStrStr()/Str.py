def strstr(haystack,needle):

	if not haystack and not needle:
		return 0
	if not haystack:
		return -1
	length = len(needle)
	for i in range(len(haystack)-length+1):
		print(haystack[i:i+length])
		if haystack[i:i+length] == needle:
			return i
	return -1

print(strstr("aaabaa", "baa"))