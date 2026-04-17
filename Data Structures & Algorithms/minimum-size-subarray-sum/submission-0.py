class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = float("inf")
        s = 0

        start = 0
        for end in range(len(nums)):
            s += nums[end]

            while s >= target:
                minL = min(end - start + 1, minL)
                s -= nums[start]
                start += 1
        
        return minL if minL != float("inf") else 0
            