class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pref, suff, res = [1] * l, [1] * l, [1] * l

        for i in range(1, l): # [1, 2, 4, 6]
            pref[i] = pref[i - 1] * nums[i - 1] # [1, 1*1, 2*1, 2*4]
        
        for i in range(l - 2, -1, -1): # [1, 2, 4, 6]
            suff[i] = suff[i + 1] * nums[i + 1] # [2*6*4, 6*4, 6*1, 1]

        for i in range(l): 
            res[i] = pref[i] * suff[i] # [0 ... i - 1] * [i + 1 ... end]

        return res