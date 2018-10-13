"""
1. DFS on each unvisited node of the graph
2. keep track of parent node 
3. For each u in v
    - if you is not visited, then DFS on u 
        -- TRUE if recursive call returns True 
4. if u is not equal to parent, then we have a cycle 
"""


#def cycle():
class DetectCycle:
    def __init__(self, vertices):
        self.V = vertices


    def is_cyclic(self):
        visited = [False] * self.V

        for v in self.graph.keys()