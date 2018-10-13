
def pal(s):
	if len(s) == 1 or len(s) == 0:
		return True
	return palindrome(s,0,len(s)-1,0)


def palindrome(s,i,j,counter):
	if i > j:
		return True
	if s[i] == s[j]:
		return palindrome(s,i+1, j-1, counter)
	else:
		if counter == 0:
			counter = 1
			if palindrome(s,i+1,j,counter):
				return True
			elif palindrome(s,i,j-1,counter):
				return True
			else:
				return False
		else:
			return False
	return False


print(pal("racecaor"))