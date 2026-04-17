class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        front, back = 1, 1
        maxi = float("-inf")

        for i in range(1, n + 1):
            front = nums[i - 1] * (front or 1)
            back = nums[n - i] * (back or 1)
            maxi = max([front, back, maxi])
        
        return maxi