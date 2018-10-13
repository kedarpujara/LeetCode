"""
Pseudocode 
    1. Initialize distances to inf
    2. Set distance from src to src to 0
    3. Push distances and corresonding vertex into the heap
    4. While heap not empty
        - pop smallest distsance vetex u from the heap 
        - iterate over neighboring vertices of u 
            -- if length from v to (u + dist[u] is smaller than our distance from the heap
            -- push new element onto the heap
"""

from collections import defaultdict
import heapq

class ShortestPath:
    def build_graph(self, edges):
        graph = defaultdict(list)
        for cost, u, v in edges:
            graph[u].append((cost, v))

    def shortest_path_dijkstra(self, edges, src, dest):
        graph = self.build_graph(edges)

        dist = defaultdict(int)
        prev = defaultdict(int)

        pq = []

        dist[src] = 0

        #All distances set to infinity except source, which is at 0
        #Add all vertex/distance to heap and push it to priority queue         
        for vertex in graph:
            if vertex != src:
                dist[vertex] = float('INF')
                prev[vertex] = None 
            heapq.heappush(pq, (dist[vertex], vertex))
        
        #Pop heap, get distances from nearby 
        while pq:
            curr, u = heapq.heappop(pq)
            for cost_u_to_v, v in graph[u]:
                curr_cost = cost_u_to_v + dist[u]
                if curr_cost < dist[v]:
                    dist[v] = curr_cost
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))
        return dist, prev


def main():
    sp = ShortestPath()
    edges = [(5,"A", "B"), (2, "B", "C"), (3,"C","D"), (9,"A","D"), (2,"A","E"),(3,"E","F"),(2,"D","F")]
    src = "A"
    dest = "C"
    dist, prev = sp.shortest_path_dijkstra(edges, src, dest)
    print(dist)

if __name__ == '__main__':
    main()
        