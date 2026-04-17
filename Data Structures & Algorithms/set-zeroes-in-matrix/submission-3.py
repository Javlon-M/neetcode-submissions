class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 0,"#","#",0
        # "#",4,5,"#"
        # "#",3,1,"#"
        # time O(n * m) n = len of colls, m = len of rows
        # space O(1)
        m, n = len(matrix), len(matrix[0])

        def bfs(i, j):
            for r in range(i + 1, m):
                if matrix[r][j] == 0: continue
                matrix[r][j] = "#"
            
            for r in range(i - 1, -1, -1):
                if matrix[r][j] == 0: continue
                matrix[r][j] = "#"

            for c in range(j - 1, -1, -1):
                if matrix[i][c] == 0: continue
                matrix[i][c] = "#"
            
            for c in range(j + 1, n):
                if matrix[i][c] == 0: continue
                matrix[i][c] = "#"
          
        for i in range(m):
            for j in range(n): 
                if matrix[i][j] == 0:
                    bfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
