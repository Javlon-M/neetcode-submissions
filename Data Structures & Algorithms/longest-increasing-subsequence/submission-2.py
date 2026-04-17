class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.maxi = 0
        memo = {}

        def dfs(i, arr):
            if i == len(nums):
                return len(arr)
            
            if i in memo:
                return memo[i] + len(arr) - 1
            
            for j in range(i, len(nums)):
                if arr[-1] < nums[j]:
                    l = dfs(j + 1, arr + [nums[j]])
                    memo[i] = max(l - len(arr) + 1, memo.get(i, 0))
                    self.maxi = max(self.maxi, l)

            return len(arr)

        for i in range(len(nums)):
            dfs(i + 1, [] + [nums[i]])

        return max(self.maxi, 1)
        
