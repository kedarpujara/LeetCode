from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph, indegree = self.build_graph(numCourses, prerequisites)

        queue = deque([course for course in range(numCourses) if indegree[course] == 0])

        top_order = deque()
        num_visited = 0
        
        while queue:
            node = queue.popleft()
            top_order.appendleft(node)


            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
            
            num_visited += 1
        
        return list(top_order) if num_visited == numCourses else []




    def build_graph(self, numCourses, prereqs):
        graph = defaultdict(set)
        indegree = [0]*numCourses
        for incoming, outgoing in prereqs:
            graph[incoming].add(outgoing)
            indegree[outgoing] += 1
        return graph, indegree

def main():
    s = Solution()
    print(s.findOrder(2, [[1,0]]))
    print(s.findOrder(2, [[1,0],[0,1]]))
    print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
main()