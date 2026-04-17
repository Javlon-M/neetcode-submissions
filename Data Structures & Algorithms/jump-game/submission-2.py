class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        n = len(nums)

        def dfs(i):
            if i >= n - 1: return True

            if nums[i] == 0: return False

            if i in memo: return memo[i]

            res = False
            for j in range(i + 1, i + nums[i] + 1):
                res = dfs(j)
                
                if res: break
            
            memo[i] = res

            return res
        
        return dfs(0)