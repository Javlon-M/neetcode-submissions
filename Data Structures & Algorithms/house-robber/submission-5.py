class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n

        def dp(i):
            if i >= n: return 0
            
            if memo[i]: return memo[i]

            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))

            return memo[i]
        
        return dp(0)