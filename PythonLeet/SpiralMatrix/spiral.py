class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        answer = []
        
        ordering = {0: "right", 1: "down", 2: "left", 3: "right"}
        self.dfs_visit(matrix,visited,ordering,0,0,0,answer)
        return answer

    def dfs_visit(self, matrix, visited, ordering, curr_order,i,j, answer):
        #GO right
        if curr_order == "right":
            if i < len(matrix) and visited[i][j] == False:
                if visited[i][j] == False:
                    visited[i][j] = True
                    answer.append(matrix[i][j])
                    self.dfs_visit(matrix,visited,ordering, curr_order, i+1,j,answer)
            else:
                current_order = "down"
                self.dfs_visit(matrix, visited, ordering, curr_order, i-1, j+1, answer)
        #GO DOWN
        elif curr_order == "down":
            if j < len(matrix[0]) and visited[i][j] == False:
                if visited[i][j] == False:
                    visited[i][j] = True 
                    answer.append(matrix[i][j])
                    self.dfs_visit(matrix, visited, ordering, curr_order, i,j+1,answer)
            else:
                curr_order = "left"
                self.dfs_visit(matrix, viisted, ordering, curr_order, i-1,j-1, answer)
        
        elif curr_order == "left":
            if i >= 0:
                if visited[i][j] = False
        