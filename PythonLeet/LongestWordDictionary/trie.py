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
			#print(node.word)
		node.isEnd = True
		node.word = word


	def bfs(self):
		queue = collections.deque([self.root])
		res = ''
		while queue:
			curr = queue.popleft()
			#print(curr.word)
			for node in curr.children.values():
				if node.isEnd:
					queue.append(node)
					if len(node.word)>len(res) or node.word <res:
						res = node.word
			print res
		return res
class Solution(object):
	def longestWord(self, words):
		trie = Trie()
		for word in words:
			trie.insert(word)

		return trie.bfs()
def main():
	solution = Solution()
	print(solution.longestWord(["w","wo","wor","worl", "world"]))
	#print(solution.longestWord(["b","ba","ban"]))

main()






