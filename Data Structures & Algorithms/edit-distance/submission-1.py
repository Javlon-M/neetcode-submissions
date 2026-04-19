class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2: return 0

        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = i
        
        for i in range(m + 1):
            dp[i][0] = i
        
        for i in range(n):
            for j in range(m):
                op = 0
                if word1[i] != word2[j]:
                    op = 1
                
                dp[j + 1][i + 1] = min(
                    dp[j][i] + op, dp[j + 1][i] + 1, dp[j][i + 1] + 1
                )
        
        return dp[-1][-1]

