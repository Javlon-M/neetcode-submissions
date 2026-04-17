class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0: return False
        if s == 0: return True
        n = len(nums)

        def dfs(i, total):
            if total == s / 2:
                return True
            if i == n:
                return False
            
            for j in range(i, n):
                if total + nums[j] <= s / 2:
                    ans = dfs(j + 1, total + nums[j])
                    if ans:
                        return True
                        
            return False
        
        return dfs(0, 0)