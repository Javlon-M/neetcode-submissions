class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        def dfs(s, i): 
            if i == len(nums): # 3 == 3   
                if s == target: # 
                    self.count += 1 # 3
                return 
            
            dfs(s + nums[i], i + 1) # 0 + 2, 0 + 1
            dfs(s - nums[i], i + 1) # 0 - 2, 0 + 1

        dfs(0, 0)
        return self.count
