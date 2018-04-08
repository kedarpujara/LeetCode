import java.util.*;
import java.io.*;

class DFS {

  private int numVertices;
  private LinkedList<Integer> adj[];


  DFS(int v){
    numVertices = v;
    adj = new LinkedList[v];
    for(int i = 0; i < v; ++i){
      adj[i] = new LinkedList();
    }
  }

  void addEdge(int v, int w){
    adj[v].add(w);
  }

  void DFSHelper(int v, boolean visited[]){
    visited[v] = true;
    System.out.print(v+"->");

    Iterator<Integer> iter = adj[v].listIterator();
    while(iter.hasNext()){
      int n = iter.next();
      if(!visited[n]){
        DFSHelper(n, visited);
      }
    }
  }

  void DFSSearch(int v){
    boolean visited[] = new boolean[numVertices];
    DFSHelper(v, visited);
    System.out.println();
  }

  public static void main(String[] args) {
    DFS g = new DFS(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    g.DFSSearch(2);
  }

}
