class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suff, pref = [1] * (n + 1), [1] * (n + 1)
        
        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        
        res = []
        for i in range(n):
            res.append(suff[i] * pref[i])
        
        return res

