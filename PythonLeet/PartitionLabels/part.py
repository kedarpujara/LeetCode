def part(s):
	curr_max = s.rfind(s[0])
	substr = ""
	solution = []
	for i in range(len(s)):
		if i <= curr_max:
			if s.rfind(s[i]) > curr_max:
				curr_max = s.rfind(s[i])
			substr += s[i]
		else:
			curr_max = s.rfind(s[i])
			solution.append(len(substr))
			substr = s[i]

	solution.append(len(substr))
	return solution


print part("ababcbacadefegdehijhklij")