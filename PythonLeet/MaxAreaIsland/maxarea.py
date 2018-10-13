class Solution:
    def maxAreaOfIsland(self, grid):
        
        max_area = 0
        curr_max = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_max_area = self.dfs(grid, i, j, curr_max)
                    #print(curr_max)
                    max_area = max(max_area, curr_max_area)
                    curr_max_area = 0
        print("")
        return max_area


    def dfs(self, grid, i,j, max_area):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return max_area
        print(max_area)
        #Check to the right 
        if i >= 0 and i < len(grid) and grid[i][j] == 1:
            #print("Here")
            grid[i][j] = 0
            max_area += 1
            self.dfs(grid,i+1,j,max_area)
        
        #Check to the right 
        if i >= 0 and i < len(grid) and grid[i][j] == 1:
            grid[i][j] = 0
            max_area += 1
            self.dfs(grid,i-1,j,max_area)

        #Check to the bottom
        if j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            max_area += 1
            self.dfs(grid,i,j+1,max_area)

        #Check to the top
        if j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
            grid[i][j] = 0
            max_area += 1
            self.dfs(grid,i,j-1,max_area)



def main():
    s = Solution()
    grid = [[0,0,1,1,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(s.maxAreaOfIsland(grid))
    #print(type(grid[0][0]))

main()