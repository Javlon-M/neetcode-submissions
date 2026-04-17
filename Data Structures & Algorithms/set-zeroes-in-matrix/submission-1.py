class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visit = set()
        n, m = len(matrix), len(matrix[0])

        def bfs(i, j):
            if not (0 <= i < n and 0 <= j < m): return

            for k in range(n):
                matrix[k][j] = 0
            
            for k in range(m):
                matrix[i][k] = 0
            
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    visit.add((i, j))
            
        for a, b in visit:
            bfs(a, b)

        