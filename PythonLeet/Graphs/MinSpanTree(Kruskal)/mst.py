from collections import defaultdict 
from sets import Set
import operator
class Graph:
    def __init__(self, edges):
        self.graph, self.vertices = self.build_graph_array(edges)

    def build_graph_array(self, edges):
        graph = []
        vertices = []
        for u,v,cost in edges:
            if u not in vertices:
                vertices.append(u)
            if v not in vertices:
                vertices.append(v)
            graph.append((u,v,cost))
        return graph, vertices

    def make_set(self, vertex, parent, rank):
        parent[vertex] = vertex
        rank[vertex] = 0
    
    
    def Kruskal(self):
        self.parent = defaultdict(int)
        self.rank = defaultdict(int)
        mst = set()
        for vertex in self.vertices:
            self.make_set(vertex, self.parent, self.rank)
        sorted_edges = sorted(self.graph, key=lambda cost: cost[2])
        #print(sorted_edges)
        
        for u,v,cost in sorted_edges:    
            #don't add duplicates        
            if self.find(u) != self.find(v):
                self.union(u, v)
                mst.add((u,v,cost))
        
        return sorted(mst)
    
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2 
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1
  
    
    def find(self, vertex):
        #Initial setup has parent[vertex] = vertex
        #If that node was accessed 
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
        
            



def main():

    edges = set([(0,1,10), (0,5,6), (0,3,5), (1,3,15), (5,3,4)])
    edges2 = set([
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
        ])
    #print(list(edges2).sort())
    g = Graph(edges2)
    print(g.graph)
    print(g.vertices)
    print("")
    print(g.Kruskal())
main()
