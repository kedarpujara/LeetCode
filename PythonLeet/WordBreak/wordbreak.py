import collections
class TrieNode(object):
	def __init__(self):
		self.children = collections.defaultdict(TrieNode)
		self.isEnd = False
		self.word = ''


class Trie(object):
	def __init__(self):
		self.root = TrieNode()


	#inserting a whole word into the trie 
	#for each character, set the child to be teh node 
	def insert(self, word):
		node = self.root
		for char in word:
			node = node.children[char]
		node.isEnd = True
		node.word = word

	def dfs(self, s):
		stack = [self.root]
		print stack.pop().word
		while stack:
			print(stack.pop().word)

class Solution(object):
	def WordBreak(self,s, wordDict):
		trie = Trie()
		for word in wordDict:
			trie.insert(word)
		return trie.dfs(s)



def main():
	sol = Solution()
	print(sol.WordBreak("applepenapple",["apple", "pen"]))

main()
