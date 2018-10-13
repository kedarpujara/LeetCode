def wordbreak(s, word_dict):
	size = len(s)
	matrix = [[False for x in range(size)] for y in range(size)]
	#print(matrix)

	for i in range(len(s)):
		for j in range(i):
			if s[j:i] in word_dict:
				matrix[j][i] = True
			else:
				for k in range(j,i-1):
					print(j)
					if matrix[j][k] == True and matrix[k+1][i-1] == True:
						matrix[j][i] = True
	print matrix
	print matrix[size-1][0]
	return matrix[size-1][0]

def wb(s, word_dict):
	size = len(s)
	matrix = [[False for x in range(size)] for y in range(size)]
	#print(matrix)

	for i in range(len(s)):
		for j in range(len(s)):
			print s[i:j+1]

print(wordbreak("iamace",["i", "am", "ace"]))
# print(wb("iamace",["i", "am", "ace"]))

#wordbreak("applepenapple",["apple", "pen"])