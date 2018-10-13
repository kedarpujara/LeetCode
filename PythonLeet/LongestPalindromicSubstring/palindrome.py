def palindrome(s):
	if not s or len(s) == 0:
		return ""
	i = 0
	length = len(s)
	diff = 0
	#for i in range(len(s)):
	substr = ""
	max_substr = ""

	
	while i < length:
		#odd cases
		while i - diff >= 0 and i + diff < length and s[i-diff] == s[i+diff]:
			substr = s[i-diff:i+diff+1]
			#print substr
			diff += 1
		if len(substr) > len(max_substr):
			max_substr = substr
		substr = ""
		diff = 0

		#even cases
		while i - diff >= 0 and i + diff + 1< length and s[i-diff] == s[i+diff+1]:
			substr = s[i-diff:i+diff+2]
			#print substr
			diff += 1
		if len(substr) > len(max_substr):
			max_substr = substr

		substr = ""
		diff = 0
		i += 1
	return max_substr

print(palindrome("babadood"))