#Look at Algorithm.txt

from collections import defaultdict

class TopologicalSort:
    def __init__(self, f):
        #self.graph = defaultdict(list)
        self.graph, self.visited = self.make_adj_list(f)
    
    """
    """
    def graph_variable(self):
        return defaultdict(list)


    """
    Making an adjacency list. Specifically for files with who's nodes/edges look like 
    A -> B 

    You can also use add_edge if you want to add it differently 
    create a visited hashmap for each node 

    """
    def make_adj_list(self, f):
        orderings = open(f)
        graph = defaultdict(list)
        visited = defaultdict(bool)
        for line in orderings:
            line = line.strip().split(' -> ')
            self.add_edge(graph, line[0], line[1])
            visited[line[0]] = False
            visited[line[1]] = False
            graph[line[1]]
        return graph, visited
            
    def add_edge(self, graph, u, v):
        graph[u].append(v)


    def topo_sort(self):
        stack = []

        for vertex in self.graph:
            if self.visited[vertex] == False:
                self.topo_sort_dfs(vertex, stack)        
        return stack

    def topo_sort_dfs(self, vertex, stack):
        print(stack)
        self.visited[vertex] = True

        children = self.graph[vertex]
        if len(children) > 0:
            for node in children:
                if self.visited[node] == False:
                    self.topo_sort_dfs(node, stack)
        stack.insert(0, vertex)


def main():
    ts = TopologicalSort("topo_graph_2.txt")
    #print(ts.graph)
    print(ts.topo_sort())

main()
