class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        queue = deque([])
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            l = len(queue)
            for _ in range(l):
                (i, j) = queue.popleft()

                for (ni, mj) in neighbors:
                    if (i + ni) >= n or (j + mj) >= m or (i + ni) < 0 or (j + mj) < 0:
                        continue
                
                    if grid[i + ni][j + mj] == 1:
                        grid[i + ni][j + mj] = 2
                        queue.append((i + ni, j + mj))
            
            if queue:
                time += 1
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return time