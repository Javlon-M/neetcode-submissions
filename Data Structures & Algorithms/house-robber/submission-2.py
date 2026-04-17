class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        def dfs(i):
            if i in dic: return dic[i]
            
            if not (0 <= i < n):
                return 0
            
            dic[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            
            return dic[i]
       
        return dfs(0)

         
