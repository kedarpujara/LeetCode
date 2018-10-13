def minpathsum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Set grid values for the first 
            if j == 0:
                if i > 0:
                    grid[i][j] = grid[i-1][j] + grid[i][j]
            else:
                if i == 0:
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]                
    return grid[len(grid)-1][len(grid[0])-1]


grid = [[1,3,1],[1,5,1],[4,2,1]]

minpathsum(grid)
