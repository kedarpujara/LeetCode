import java.util.*;
import java.io.*;

class BFS {

  private int numVertices;
  private LinkedList<Integer> adj[];

  BFS(int v){
    numVertices = v;
    adj = new LinkedList[v];
    for(int i = 0; i < v; i++){
      adj[i] = new LinkedList();
    }
  }

  void addEdge(int v, int w){
    adj[v].add(w);
  }

  void BFSearch(int v){
    boolean visited[] = new boolean[numVertices];
    LinkedList<Integer> queue = new LinkedList<Integer>();

    visited[v] = true;
    queue.add(v);
    while(queue.size() != 0){
      int top = queue.poll();
      System.out.print(top+"->");
      Iterator<Integer> iter = adj[v].listIterator();
      while(iter.hasNext()){
        int n = iter.next();
        if(!visited[n]){
          visited[n] = true;
          queue.add(n);
        }
      }
    }
    System.out.println();


  }


  public static void main(String[] args) {
    BFS g = new BFS(4);

    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    g.BFSearch(0);
  }



}
