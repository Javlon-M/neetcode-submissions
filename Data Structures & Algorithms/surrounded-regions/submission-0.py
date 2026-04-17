class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        
        def dfs(i, j):
            if i >= n or j >= m or i < 0 or j < 0 or board[i][j] != 'O':
                return

            board[i][j] = "#" 

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
        for i in range(n):
            for j in range(m):
                if (i in (0, n - 1) or j in (0, m - 1)) and board[i][j] == 'O':
                    dfs(i, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == "#":
                    board[i][j] = 'O'
        