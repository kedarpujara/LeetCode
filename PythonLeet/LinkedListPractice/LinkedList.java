public class Node {
	protected Node next;
	protected int data;

	public Node(){
		next = null;
		data = 0;
	}

	public Node(Node link, int d) {
		this.next = link;
		this.data = d;
	}

	public void setData(int d) {
		this.data = d;
	}

	public void setNext(Node n) {
		this.next = n;
	}

	public void getNext() {
		return next;
	}

	public void getData() {
		return data;
	}
}


public class LinkedList {
	protected Node head;
	protected Node end;
	public int size;

	public LinkedList(){
		this.head = null;
		this.end = null;
		this.size = 0;
	}

	public int getSize(){
		return size;
	}

	public boolean isEmpty(){
		return start==null;
	}

	public void insertAtBeginning(int val) {
		Node newNode = Node(null, val);
		size++;
		if (start == null) {
			start = newNode;
			end = start;
		} else{
			newNode.setNext(start);
			start = newNode;
		}
	}

	public void insertAtEnd(int val) {
		Node newNode = Node(null, val);
		size++;
		if (start == null) {
			start = newNode;
			end = start;
		} else {
			end.setNext(newNode);
			end = newNode;
		}
	}

	public void insertAtIndex(int val, int pos){
		Node newNode = Node(null, val);
		Node ptr = start;
		for (int i = 0; i < pos; i++) {
			ptr = start.next;
		}
		temp = ptr.getNext();
		ptr.setNext(newNode);
		newNode.setNext(temp);
	}

	public void deleteAtPosition(int pos) {
		if(pos == 1) {
			start.setNext()
		}
	}







}