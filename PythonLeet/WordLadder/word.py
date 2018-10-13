from Queue import *

def isDiffOne(s1,s2):
	counter = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			if counter == 0:
				counter += 1
			else:
				return False
	return True

def wordLadder(begin_word, end_word, word_list):
	counter = 0

	q = Queue()
	q.put(begin_word)
	
	while q.empty() != True:
		
		s = q.get()
		print word_list
		print s
		print ""
		if s == end_word:
			return counter
		for word in word_list:
			if isDiffOne(s,word):
				if word == end_word:
					return counter
				q.put(word)
				word_list.remove(word)
				counter += 1
		
	return 0


#print(isDiffOne("hoa", "hit"))
#print(wordLadder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(wordLadder("hit", "cog", ["hot","dot","dog","lot","log"]))