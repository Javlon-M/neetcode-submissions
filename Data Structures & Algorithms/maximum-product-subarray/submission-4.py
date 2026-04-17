class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        front, back = 1, 1
        maxi = float("-inf")

        for i in range(1, n + 1):
            if front == 0: front = 1
            if back == 0: back = 1

            front *= nums[i - 1]
            back *= nums[n - i]
            maxi = max([front, back, maxi])
        
        return maxi