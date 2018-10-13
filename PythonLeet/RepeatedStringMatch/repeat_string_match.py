def repeat(a,curr_a, b, num_repeats):
	while is_substr(curr_a,b) == False:
		print("here")
		curr_a += a
		print(curr_a)
		num_repeats += 1
		
	
	print("")
	return num_repeats + 1

def repeat_string_match(a,b):
	return repeat(a,a,b,0)


def is_substr(a,b):
	b_len = len(b)
	a_len = len(a)
	if a_len < b_len:
		return False
	else:
		for i in range(len(a)-len(b)+1):
			#print(a[i:i+b_len])
			if a[i:i+b_len] == b:
				return True
	return False

print(repeat_string_match("abc", "abcabcabcabc"))

print(repeat_string_match("abcd", "cdabcdab"))