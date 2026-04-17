class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)

        n = len(nums) + 1

        i = 0

        while i <= n:
            if i not in s: return i
            i += 1