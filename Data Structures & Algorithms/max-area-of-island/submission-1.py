class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxi = 0
        n, m = len(grid), len(grid[0])

        def dfs(i, j, count):
            if i >= n or j >= m or grid[i][j] != 1 or j < 0 or i < 0:
                return count
            
            count += 1
            self.maxi = max(self.maxi, count)
            grid[i][j] = -1
            
            count = dfs(i - 1, j, count)
            count = dfs(i + 1, j, count)
            count = dfs(i, j - 1, count)
            count = dfs(i, j + 1, count)

            return count

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j, 0)

        return self.maxi