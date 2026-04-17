LAND = "1"
WATER = "0"

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands, n, m = 0, len(grid), len(grid[0])

        def dfs(i, j):
            visited.add((i, j))

            neighboars = [
                (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
            ]

            for ni, nj in neighboars:
                if (ni, nj) in visited: continue
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == LAND:
                    dfs(ni, nj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == LAND and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1
        
        return islands