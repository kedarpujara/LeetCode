from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.vertices = V
        self.graph = defaultdict(list)
    
    def add_edge(self, incoming, out, cost):
        self.graph[incoming].append((out, cost))


    def topological_sort_util(self, node, visited, stack):
        visited[node] = True 
        if node in self.graph.keys():
            for vertex, weight in self.graph[node]:
                if visited[vertex] == False:
                    self.topological_sort_util(vertex, visited, stack)
        stack.append(node)

    def shortest_path(self, start):
        visited = [False] * self.vertices
        stack = []


        for i in range(self.vertices):
            if visited[i] == False:
                self.topological_sort_util(s,visited,stack)


        dist = [float("Inf")] * (self.vertices)
        print(dist)

        dist
