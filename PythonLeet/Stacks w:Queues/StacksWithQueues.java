import java.io.*;
import java.util.*;

public class StacksWithQueues<E> {

	private Stack<E> inbox = new Stack<E>();
	private Stack<E> outbox = new Stack<E>();

	public void push(E item) {
		inbox.push(item);
	}

	public E dequeue() {
		if (outbox.isEmpty()) {
			while(!inbox.isEmpty()) {
				outbox.push(inbox.pop());
			}

		}
		return outbox.pop();
	}


}