class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = [[-1]*len(text2) for _ in range(len(text1))]
        
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if self.memo[i][j] != -1:
                return self.memo[i][j]
            
            if text1[i] == text2[j]:
                self.memo[i][j] = dfs(i + 1, j + 1) + 1
                return self.memo[i][j]
            
            self.memo[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return self.memo[i][j]
        
        return dfs(0, 0)