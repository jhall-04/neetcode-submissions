class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ct = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ct += 1
                    self.dfs(i, j, grid)
        return ct
                

    def dfs(self, x, y, grid):
        if 0 <= x <= len(grid)-1 and 0 <= y <= len(grid[0])-1:
            if grid[x][y] == '1':
                grid[x][y] = '0'
                self.dfs(x+1, y, grid)
                self.dfs(x, y+1, grid)
                self.dfs(x-1, y, grid)
                self.dfs(x, y-1, grid)
        return
        
