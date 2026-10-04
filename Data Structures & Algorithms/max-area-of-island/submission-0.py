class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        max_area=0
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0:
                return 0
            grid[i][j]=0
            area=1
            area+=dfs(i-1,j)
            area+=dfs(i+1,j)
            area+=dfs(i,j-1)
            area+=dfs(i,j+1)
            return area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    area=dfs(i,j)
                    max_area=max(max_area,area)
        return max_area