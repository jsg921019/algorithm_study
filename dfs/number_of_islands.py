# https://leetcode.com/problems/number-of-islands/

# Easy

# recurrsion

class Solution:
    
    def dfs(self, i, j, grid):
        grid[i][j] = '0'
        if i < len(grid)-1 and grid[i+1][j] == '1':
            self.dfs(i+1, j, grid)
        if j < len(grid[0])-1 and grid[i][j+1] == '1':
            self.dfs(i, j+1, grid)
        if 0 < i and grid[i-1][j] == '1':
            self.dfs(i-1, j, grid)
        if 0 < j and grid[i][j-1] == '1':
            self.dfs(i, j-1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    num_island += 1
        return num_island

# iteration

class Solution:
    
    def dfs(self, i, j, grid):
        stack = [(i,j)]
        while stack:
            x, y = stack.pop()
            for x_, y_ in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= x_ < len(grid) and 0 <= y_ < len(grid[0]) and grid[x_][y_] == '1':
                    stack.append((x_, y_))
                    grid[x_][y_] = '0'

    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid)
                    num_island += 1
        return num_island