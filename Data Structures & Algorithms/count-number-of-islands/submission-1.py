class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
                return

            grid[i][j] = "#"

            neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for [x, y] in neighbors:
                dfs(i + x, j + y)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count