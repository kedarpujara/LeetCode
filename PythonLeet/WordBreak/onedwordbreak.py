def onewordbreak(s, word_list):
	bool_ar = [False for x in range(len(s)+1)]
	bool_ar[0] = True

	for i in range(1,len(s)+1):
		for j in range(i):
			if s[j:i] in word_list and bool_ar[j] == True:
				bool_ar[i] = True
				print i 
				break
			else:
				bool_ar[i] = False
		#print("")
	print bool_ar
	print bool_ar[-1]
	return bool_ar[-1]

onewordbreak("wordbreak", ["word", "break"])

onewordbreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])


print len("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

# Output: true)

# # ar = ["i", "am", "ace"]
# # if "" in ar:
# # 	print True
# # else:
# # 	print

#print 7//3
