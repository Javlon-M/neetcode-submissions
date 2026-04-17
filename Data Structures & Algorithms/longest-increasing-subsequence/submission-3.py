class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.maxi = 0
        memo = {}

        def dfs(i, arr):
            for j in range(i, len(nums)):
                if arr[-1] < nums[j]:
                    l = dfs(j, arr + [nums[j]])
                    
                    self.maxi = max(self.maxi, l)

            return len(arr)

        for i in range(len(nums)):
            dfs(i, [nums[i]])

        return max(self.maxi, 1)
        
