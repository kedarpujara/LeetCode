def permute(s):
	res = []	
	permuteHelper(res,s,"")
	return res


def permuteHelper(res,s,curr):
	if s == "":
		res.append(curr)
	else:
		for i in range(len(s)):
			curr += s[i]
			copy_s = s[:i] + s[i+1:]
			permuteHelper(res, copy_s, curr)
			s = s[:i] + s[i:]
			curr = curr[:-1]
print(permute("abc"))


s = "hello"
i = 1
copy_s = s[:i] + s[i+1:]
print(copy_s)