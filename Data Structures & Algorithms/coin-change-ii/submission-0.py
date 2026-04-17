class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, total):
            if i == len(coins) or total > amount:
                return 0

            if total == amount:
                return 1
            
            if (total, i) in memo:
                return memo[(total, i)]

            ways = 0
            for j in range(i, len(coins)):
                ways += dfs(j, total + coins[j])
            
            memo[(total, i)] = ways

            return ways

        return dfs(0, 0)