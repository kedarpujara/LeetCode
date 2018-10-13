def concat_substrs(s, words):
	length = len(words[0])
	num_words = len(words)
	temp = words
	solution = []
	i = 0
	initial_i = 0
	while i < len(s):
		while s[i:i+length] in temp:
			print(temp)
			print(s[i:i+length])
			temp.remove(s[i:i+length])
			i += length
			if len(temp) == 0:
				solution.append(initial_i)
		temp = words
		print(words)
		print("hello")
		i += length
		initial_i = i
		print(solution)
		print(i)
		print("")
	return solution

def create_dict(words):
	word_map = {}
	for word in words:
		if word in word_map:
			word_map[word] += 1
		else:
			word_map[word] = 1
	return word_map

def concat(s, words):
	curr_end = len(words) * len(words[0])
	chunk_size = curr_end / len(words)
	word_map = create_dict(words)
	curr_index = 0
	solution = []
	
	i = 0
	substring = []
	while i < len(s):
		for j in range(curr_index,curr_end,chunk_size):
			substring.append(s[j:j+chunk_size])
		
		curr_word_map = create_dict(substring)

		if curr_word_map == word_map:
			#print("hello")
			solution.append(curr_index)
			#print(curr_index)
		
		substring = []
		
		i += 1
		curr_end += 1
		curr_index += 1
		
	print solution
	return solution


concat("barfoothefoobarman", ["foo", "bar"])
concat("wordstudgoodstudword", ["word","stud"])
concat("lingmindraboofooowingdingbarrwingmonkeypoundcake",
["fooo","barr","wing","ding","wing"])



