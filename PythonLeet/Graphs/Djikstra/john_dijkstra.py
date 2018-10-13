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


def build_graph(edges):
    graph = defaultdict(list)
    for cost,u,v in edges:
        graph[u].append((cost,v))
    return graph


def dijkstra(edges, src):
    #S = set()
    graph = build_graph(edges)

    dist = defaultdict(int)
    prev = defaultdict(int)

    priority_q = [] #Heap in form of priority queue
    dist[src] = 0

    # Set all distances to infinitey
    for v in graph.keys():
        if v != src:
            dist[v] = float('inf')
            prev[v] = None 
        heapq.heappush(priority_q,(dist[v], v))
    

    while priority_q:
        length, u = heapq.heappop(priority_q)

        for cost_u_to_v, v in graph[u]:
            alt = dist[u] + cost_u_to_v 
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(priority_q, (alt,v))
    
    return dist, prev 





def main():
    edges = [(5,"A", "B"), (2, "B", "C"), (3,"C","D"), (9,"A","D"), (2,"A","E"),(3,"E","F"),(2,"D","F")]
    #edges = [(3,"a", "b"), (4, "b", "c"), (9, "a", "d"), (1, "c", "d")]

    src = "A"
    # dest = "C"
    dist, prev = dijkstra(edges, src)
    print(dist)
    print(prev)
main()