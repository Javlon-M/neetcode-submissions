class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        front, back = 0, 0
        maxi = float("-inf")
        n = len(nums)

        for i in range(n):
            front = max(front + nums[i], nums[i])
            back = max(back + nums[n - 1 - i], nums[n - 1 - i])

            maxi = max(maxi, max(front, back))
        
        return maxi