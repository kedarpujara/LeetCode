from collections import defaultdict

class Graph:
    def __init__(self, dependencies):
        self.graph, self.visited = self.build_graph(dependencies)
    

    def topological(self):
        stack = []
        print(self.graph)
        for vertex in self.graph:
            print(vertex)
            if self.visited[vertex] == False:
                self.dfs(vertex, stack)
        return stack
    
    def dfs(self, vertex, stack):
        self.visited[vertex] = True
        children = self.graph[vertex]
        if len(children) > 0:
            for child in children:
                if self.visited[child] == False:
                    self.dfs(child, stack)
        stack.insert(0,vertex)

    def build_graph(self, dependencies):
        graph = defaultdict(list)
        visited = defaultdict(bool)
        for pair in dependencies:
            graph[pair[0]].append(pair[1])
            graph[pair[1]]
            visited[pair[0]] = False 
            visited[pair[1]] = False
        return graph, visited


def main():
    depend = [("a","d"), ("f","b"), ("b","d"), ("f","a"), ("d","c")]
    g = Graph(depend)
    print(g.topological())
    

main()
