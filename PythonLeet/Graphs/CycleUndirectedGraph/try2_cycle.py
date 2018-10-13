from collections import defaultdict

class CycleGraph:
    def __init__(self, f):
        #self.graph = defaultdict(list)
        self.graph, self.visited, self.recursion_stack = self.make_adj_list(f)
    
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
        recursion_stack = defaultdict(bool)
        for line in orderings:
            line = line.strip().split(' -> ')
            self.add_edge(graph, line[0], line[1])
            visited[line[0]] = False
            visited[line[1]] = False
            recursion_stack[line[0]] = False
            recursion_stack[line[1]] = False 
            graph[line[1]]
        return graph, visited, recursion_stack
            
    def add_edge(self, graph, u, v):
        graph[u].append(v)


    def has_cycle(self):
        for vertex in self.graph:
            if self.visited[vertex] == False:
                if self.cycle_dfs(vertex):
                    return True 
        return False

    def cycle_dfs(self, vertex):        
        self.visited[vertex] = True 
        
        for child in self.graph[vertex]:                
            if self.recursion_stack[child] == True:
                return True 
            else:
                self.recursion_stack[child] = True
                if self.visited[child] == False:        
                    self.cycle_dfs(child)

        self.recursion_stack[vertex] = False
        return False




def main():
    cycle = CycleGraph("graph2.txt")
    print(cycle.graph)
    print(cycle.visited)
    #print(cycle.recursion_stack)
    print(cycle.has_cycle())

main()
