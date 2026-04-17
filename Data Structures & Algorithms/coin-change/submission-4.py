class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def dfs(amount):
            if amount == 0: return 0

            if amount in memo: return memo[amount]

            count = float("inf")
            for i in range(n):
                if amount - coins[i] >= 0:
                    count = min(1 + dfs(amount - coins[i]), count)
            memo[amount] = count
            return count

        return -1 if dfs(amount) == float("inf") else dfs(amount)