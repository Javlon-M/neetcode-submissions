class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(s, i): 
            if i == len(nums):
                return s == target

            if (s, i) in memo:
                return memo[(s, i)]
            
            memo[(s, i)] = dfs(s + nums[i], i + 1) + dfs(s - nums[i], i + 1)
            
            return memo[(s, i)]

        
        return dfs(0, 0)
