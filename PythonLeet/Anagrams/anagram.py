import collections
def anagram(s1, s2):
	if len(s1) != len(s2):
		return False
	if len(s1) == 0:
		return True

	word_dict = {}

	for i in range(len(s1)):
		if s1[i] in word_dict:
			word_dict[s1[i]] += 1
		else:
			word_dict[s1[i]] = 1

	for i in range(len(s2)):
		if s2[i] not in word_dict:
			return False
		else:
			word_dict[s2[i]] -= 1
			
	for word in word_dict:
		if word_dict[word] != 0:
			return False
	return True

print(anagram("face", "afce"))