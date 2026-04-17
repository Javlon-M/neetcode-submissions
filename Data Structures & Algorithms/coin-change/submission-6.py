class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def dfs(amount):
            if amount == 0: return 0

            if amount in memo: return memo[amount]

            count = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    count = min(1 + dfs(amount - coin), count)
            
            memo[amount] = count

            return memo[amount]
        
        
        res = dfs(amount)

        return res if res != float("inf") else -1