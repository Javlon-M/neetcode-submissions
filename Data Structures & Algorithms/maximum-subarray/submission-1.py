class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        front = 0
        maxi = float("-inf")
        n = len(nums)

        for i in range(n):
            front = max(front + nums[i], nums[i])

            maxi = max(maxi, front)
        
        return maxi