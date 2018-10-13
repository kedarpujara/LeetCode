import re
from collections import Counter
def common(s, banned):
	words = re.split(r'\W',s.lower())

	counter = {}
	max_count = 1
	most_common = ""

	for word in words:
		if word == "" or word in banned: continue
		if word not in counter:
			counter[word] = 1
		else:
			counter[word] += 1
			if counter[word] > max_count:
				max_count = counter[word]
				most_common = word
	return most_common




para = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']

print(common(para, banned))