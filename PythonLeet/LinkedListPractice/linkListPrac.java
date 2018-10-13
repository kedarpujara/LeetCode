class Node {

	Node next = null;
	int data;

	public Node(int d) {
		data = d;
	}

	public void removeDups(Node n, int d) {
		HashSet<Integer> set = new HashSet<Integer>();
		LinkedListNode prev = null;
		prev.data = d;
		while (n != null ) {
			if set.contains(n.data)
		}
	}

}