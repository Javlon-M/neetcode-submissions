class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dic = {}
        
        def dfs(amount): 
            if amount == 0: return 0

            if amount in dic: return dic[amount]

            ans = float("inf")

            for i in range(n):
                if coins[i] <= amount:
                    ans = min(ans, 1 + dfs(amount - coins[i]))

            dic[amount] = ans
            
            return ans



        ans = dfs(amount) 

        if ans == float("inf"): return -1

        return ans