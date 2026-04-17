class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        output = 0

        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] != 1:
                return 0

            neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            area = 1
            grid[i][j] = 2
            for [x, y] in neighbors:
                area += dfs(i + x, j + y)

            return area

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    output = max(area, output)

        return output
