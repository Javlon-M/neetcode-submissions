class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.maxi = 0
        memo = {}

        def dfs(i, arr):
            if i == len(nums):
                return 0
            
            if i in memo:
                return memo[i] + len(arr)
                
            for j in range(i, len(nums)):
                if arr[-1] < nums[j]:
                    l = dfs(j, arr + [nums[j]])
                    
                    memo[i] = max(l - len(arr), memo.get(i, 0))
                    self.maxi = max(self.maxi, l)

            memo[i] = memo.get(i, 0)
            return len(arr)

        for i in range(len(nums)):
            dfs(i, [nums[i]])

        return max(self.maxi, 1)
        
