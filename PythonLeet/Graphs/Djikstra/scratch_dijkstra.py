from collections import defaultdict
import heapq
class Graph:
    def __init__(self, edges):
        self.graph, self.prev, self.dist = self.create_graph(edges)

    

    def create_graph(self, edges):
        graph = defaultdict(list)
        prev = defaultdict(int)
        dist = defaultdict(int)
        
        for cost, u, v in edges:
            graph[u].append((cost, v))
            dist[v] = float("INF")
                      
        
        return graph, prev, dist

    def shortest_path(self, src):
        pq = []

        self.dist[src] = 0
        heapq.heappush(pq, src)
        while pq:
            curr = heapq.heappop(pq)
            for cost, node in self.graph[curr]:
                if (cost + self.dist[curr]) < self.dist[node]:
                    self.dist[node] = cost + self.dist[curr]
                    self.prev[node] = curr 
                    heapq.heappush(pq, node)
        return self.dist, self.prev
    
    
    

def main():
    #edges = [(3,"a", "b"), (4, "b", "c"), (9, "a", "d"), (1, "c", "d")]
    edges = [(5,"A", "B"), (2, "B", "C"), (3,"C","D"), (9,"A","D"), (2,"A","E"),(3,"E","F"),(2,"D","F")]

    g = Graph(edges)
    print(g.graph)
    #print(g.dist)
    prev, dist = g.shortest_path("A")
    print(dist)
    print(prev)
main()