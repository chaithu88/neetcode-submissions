from collections import deque
INF=2147483647
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    queue.append((i,j))
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==INF:
                    grid[nr][nc]=grid[r][c]+1
                    queue.append((nr,nc))
               