"""
Set all distances to infinity 
Set all prevs to null 

H = makequeue(Vertices)

while H:
    u = delete min(H)
    for all edges (u,v) in edges:
        if dist(v) > dist(u) + length(u,v):
            dist(v) = dist(u) + length(u,v)
            prev(v) = u #node before it on the shortest path 
            decreasekey(H,v)


DATA STRUCTURE: priority queue (impleneted via heap)
- insert 
- decrease key 
- delete min 
- make queue 

"""

from collections import defaultdict, deque
from heapq import *

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)
    
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

def djikstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node 
                elif visited[node] < visited[min_node]:
                    min_node = node 
        
        if min_node is None:
            break 
        
        nodes.remove(min_node)
        curr_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = curr_weight + graph.distances[(min_node, edge)]
            except:
                continue 
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
        print(visited)
    return visited, path
        
        
def shortest_path(graph, origin, dest):
    visited, paths = djikstra(graph, origin)
    full_path = deque()

    _dest = paths[dest]

    while _dest != origin:
        full_path.appendleft(_dest)
        _dest = paths[_dest]
    
    full_path.appendleft(origin)
    full_path.append(dest)

    return visited[dest], list(full_path)


if __name__ == '__main__':
    graph = Graph()

    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        graph.add_node(node)

    graph.add_edge('A', 'B', 10)
    graph.add_edge('A', 'C', 20)
    graph.add_edge('B', 'D', 15)
    graph.add_edge('C', 'D', 30)
    graph.add_edge('B', 'E', 50)
    graph.add_edge('D', 'E', 30)
    graph.add_edge('E', 'F', 5)
    graph.add_edge('F', 'G', 2)

    print(shortest_path(graph, 'A', 'G'))






# def djikstra(edges, from_node, to_node):
#     graph = defaultdict(list)
#     for f, t, cost in edges:
#         graph[f].append((cost,t))
    

#     queue = [(0,from_node, ())]
#     seen = Set()
#     mins = {from_node:0}

#     while queue:
#         (cost, v1,path) = heappop(queue)
#         if v1 not in seen:
#             seen.add(v1)
#             path = (v1, path)
#             if v1 == 

    