from collections import defaultdict
# class Solution(object):
#     def findOrder(self, numCourses, prerequisites):
#         self.graph = self.build_graph(prerequisites)
#         self.visited = [0 for x in xrange(numCourses)]
#         self.res = []
#         for x in xrange(numCourses):
#             if not self.DFS(x):
#                 return []
#         return self.res

#     def DFS(self, node):
#         if self.visited[node] == -1:
#             return False 
#         if self.visited[node] == 0:
#             return True 
        
#         self.visited[node] = -1

#         for x in self.graph[node]:
#             if not self.DFS(x):
#                 return False 

#         self.visited[node]
#         self.res.append(node)
#         return True 

#     def build_graph(self, prerequisites):
#         graph = defaultdict(list)
#         for pair in prerequisites:
#             graph[pair[0]].append(pair[1])
#         return graph

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        # use DFS to parse the course structure
        self.graph = defaultdict(list) # a graph for all courses
        self.res = [] # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) 
        self.visited = [0 for x in xrange(numCourses)] # DAG detection 
        for x in xrange(numCourses):
            if not self.DFS(x):
                return []
             # continue to search the whole graph
        return self.res
    
    def DFS(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        self.visited[node] = 1 # mark as finished
        self.res.append(node) # add to solution as the course depenedent on previous ones
        return True


def main():
    s = Solution()
    print(s.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
    
main()