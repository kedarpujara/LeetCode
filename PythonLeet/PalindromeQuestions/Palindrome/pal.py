def pal(s):
	lo = 0
	hi = len(s)-1

	while lo <= hi:
		if s[lo] != s[hi]:
			return False
		else:
			lo += 1
			hi -= 1
	return True

print(pal('bullub'))