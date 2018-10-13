from collections import defaultdict
from sets import Set
class Graph:
    def __init__(self):
        self.graph, self.visited = self.get_adj_list("topo_graph_2.txt")


    def get_adj_list(self, f):
        topo_file = open(f)
        graph = defaultdict(list)
        visited = defaultdict(bool)

        for line in topo_file:
            line = line.strip().split(' -> ')            
            graph[line[0]].append(line[1])
            visited[line[0]] = False
            #visited[line[1]] = False

        print(graph)
        print(visited)
        return graph, visited
        

    def random_test(self):
        for i in self.graph['1']:
            print i
        return 1
    
    def topo_sort(self):
        stack = []
        
        for vertex in self.graph:
            if self.visited[vertex] == False:
                self.topo_sort_helper(vertex, self.visited, stack)
        return ', '.join(stack)

    def topo_sort_helper(self, vertex, visited, stack):
        self.visited[vertex] = True
        #print(self.graph[vertex])
        children = self.graph[vertex]
        print(children)
        if len(children) > 0:
            for node in self.graph[vertex]:
                print(node)
                print("")
                if node in visited:
                    if self.visited[node] == False:
                        self.topo_sort_helper(node, self.visited, stack)
                    
        stack.insert(0, vertex)


def main():
    g = Graph()    
    #print(g.random_test())
    print(g.topo_sort())


main()
    # def __init__(self, vertices):
    #     self.graph = defaultdict(list)
    #     self.V = vertices
    
    # def add_edge(self, u, v):
    #     self.graph[u].append(v)







    
    # def topological_sort_helper(self, vertex, visited, stack):
    #     #print(stack)
    #     visited[vertex] = True 
    #     print(vertex)
    #     print(self.graph[vertex])
    #     print("")
        
    #     for i in self.graph[vertex]:
    #         if visited[i] == False:
    #             self.topological_sort_helper(i, visited, stack)
        
    #     stack.insert(0,vertex) #if all adjacent neighbors visited, add it to stack
    

    # def topological_sort(self):
    #     visited = [False]*self.V
    #     #print(visited)
    #     #print(self.V)
    #     stack = []

    #     for i in range(self.V):
    #         if visited[i] == False:
    #             self.topological_sort_helper(i,visited, stack)
    #     #print stack


# def main():
#     g = Graph(6)
#     g.add_edge(4, 0)
#     g.add_edge(4, 1)
#     g.add_edge(5, 2)
#     g.add_edge(5, 0)
#     g.add_edge(2, 3)
#     g.add_edge(3, 1)
#     print(g)
#     g.topological_sort()

# main()





# class TopologicalSort(object):

#     def topSort(self, graph):
#         stack = deque()
#         visited = Set()
#         for vertex in graph.vertices():
#             if vertex in visited:
#                 continue
#             self.topSortHelper(vertex,stack,visited)
#         return stack
    
    
#     def topSortHelper(self,vertex, stack, visited):
#         visited.add(vertex) #Add vertex to visited set 
#         for adjacent_vertices


