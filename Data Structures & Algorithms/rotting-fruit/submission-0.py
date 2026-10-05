from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        minutes=0
        queue=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        directions=[[1,0],[-1,0],[0,-1],[0,1]]
        while fresh>0 and queue:
            size=len(queue)
            for i in range(size):
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        queue.append((nr,nc))
                        fresh-=1
            minutes+=1 
        
        return minutes if fresh==0 else -1          
