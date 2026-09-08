class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        pref = suff = 0

        for i in range(n):
            pref = nums[i] * (pref or 1)
            suff = nums[n - 1 - i] * (suff or 1)
            res = max(res, max(pref, suff))

        return res