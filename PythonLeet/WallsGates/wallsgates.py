# class Solution:
#     def wallsAndGates(self, rooms):

# a = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# print a[0][1]

from collections import deque

class Cell:
    def __init__(self,m,n):
        self.x = m 
        self.y = n   

class Solution:
          
    def wallsAndGates(self, rooms):
        moves = [[1,0], [0,1], [-1,0], [0,-1]]
        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    c = Cell(i,j)
                    queue.append(c)
        while queue:
            temp = queue.popleft()
            x = temp.x 
            y = temp.y
            for i in range(4):
                self.bfs(x + moves[i][0],y+moves[i][1],rooms, queue, rooms[x][y]+1)
        return 

    def bfs(self,x,y,rooms,queue,steps):
        if x < 0 or y < 0 or x >= len(rooms) or y >= len(rooms[0]) or rooms[x][y] == -1 or rooms[x][y] != 2147483647:
            return 
        rooms[x][y] = steps
        queue.append(Cell(x,y))



def main():
    s = Solution()
    s.wallsAndGates(1)

main()

