from sets import Set
"""
White set, gray set, black set
If all vertices in black set, none in gray set..no cycle. Else cycle is preset 


1. Put all vertices in white set 
2. Pop a vertex randomly and put it in gray set 
3. Explore neighbors
    - If neighbor is in black set, no need to explore that neighbor 
4. If no more nieghbors, move from gray to black set 
5. 
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = self.make_graph()

    def make_graph(self):
        graph = defaultdict(list)
        graph[4] = [1,5]
        graph[1] = [2]
        graph[5] = [6]
        graph[6] = [4]
        #graph[2] = []
        print(graph)
        return graph


    def hasCycle(self):
        visited = [False] * len(self.graph)
        recursion_stack = visited
        
        for node in range(len(self.graph)):
            if visited[node] == False:
                if self.hasCycleUtil(node, visited, recursion_stack):
                    return True
        return False
    
    def hasCycleUtil(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True


        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.hasCycleUtil(neighbor, visited, rec_stack):
                    return True 
        rec_stack[v] = False
        return False 







    def has_cycle(self):
        white_set = Set()
        gray_set = Set()
        black_set = Set()

        for vertex in self.graph:
            white_set.add(vertex)

        while white_set:
            for curr_vertex in white_set:
                if self.dfs(curr_vertex, white_set, gray_set, black_set):
                    return True
        return False


    def dfs(self, curr_vertex, white_set, gray_set, black_set):
        self.move_vertex(curr_vertex, white_set, gray_set)
        for neighbor in self.graph[curr_vertex]:
            if neighbor in black_set:
                continue
            if neighbor in gray_set:
                return True
            if(self.dfs(neighbor, white_set, gray_set, black_set)):
                return True
        self.move_vertex(curr_vertex, gray_set, black_set)


    def move_vertex(self, vertex, source, destination):
        source.remove(vertex)
        destination.add(vertex)
            
def main():
    g = Graph()

    print(g.hasCycle())
main()