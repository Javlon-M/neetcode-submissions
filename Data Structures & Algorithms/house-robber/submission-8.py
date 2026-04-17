class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        memo = {}
        def dfs(i):
            if i >= l: return 0

            if i in memo: return memo[i]

            res = max(dfs(i + 2) + nums[i], dfs(i + 1))

            memo[i] = res

            return res

        return dfs(0)