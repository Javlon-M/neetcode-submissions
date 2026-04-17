class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total, dummy = 0, 0
        i = 0
        while i < n:
            total += i
            dummy += nums[i]
            i += 1

        return total + i - dummy