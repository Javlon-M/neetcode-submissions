class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
       C
    B  D  A
       A  T  A
        """
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m, n = len(board), len(board[0])

        def dfs(i, j, k, visiting):
            if k == len(word): return True

            visiting.add((i, j))
            for ni, nj in neighbors:
                if not (0 <= (i + ni) < m and 0 <= (j + nj) < n): continue
                
                if (i + ni, j + nj) in visiting: continue

                if board[i + ni][j + nj] == word[k]:
                    res = dfs(i + ni, j + nj, k + 1, visiting)
                    if res: return True
            
            visiting.remove((i, j))
        
            return False

                
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = dfs(i, j, 1, set())

                    if res: return True
                    
        return False

        