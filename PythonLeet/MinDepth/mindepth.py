from Queue import *
def min_depth(root):
	q = Queue()
	q.add(root)
	depth = 0
	while q.isempty() == False:
		size = q.size()
		temp = q.poll()
		for i in range(size):
			if not temp.left and not temp.right:
				return depth
			elif temp.left:
				q.add(temp.left)
			elif temp.right:
				q.add(temp.right)

