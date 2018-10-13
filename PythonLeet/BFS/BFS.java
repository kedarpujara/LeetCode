import java.io.*;
import java.util.*;


class Graph {

	private int V;
	private LinkedList<Integer> adj[];

	//Constructor 
	Graph(int v) {
		V = v;
		adj = new LinkedList[v];
		for(int i = 0; i < v; ++i) 
			adj[i] = new LinkedList();
	}

	//Function to add an edge into graph 
	void addEdge(int v, int w) {
		adj[v].add(w);
	}

	//BFS traversal from source s
	void BFS(int s) {

		boolean visited[] = new boolean[V];

		LinkedList<Integer> queue = new LinkedList<Integer>();

		visited[s] = true; //visited source
		queue.add(s); //add queue to source

		while(queue.size() != 0) {
			s = queue.poll(); //new node 
			System.out.println(s+ " ");

			Iterator<Integer> i = adj[s].listIterator();
			while(i.hasNext()) {
				int n = i.next();
				if(!visited[n]) {
					visited[n] = true;
					queue.add(n);
				}
			}
		}


	}


	public static void main(String[] args) {
		Graph g = new Graph(4);
		g.addEdge(0,1);
		g.addEdge(0,2);
		g.addEdge(1,2);
		g.addEdge(2,0);
		g.addEdge(2,3);
		g.addEdge(3,3);

		g.BFS(2);
	}


}