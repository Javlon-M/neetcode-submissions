class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        front, back = 1, 1
        maxi = float("-inf")
        n = len(nums)
        for i in range(n):
            if front == 0: front = 1
            if back == 0: back = 1

            front *= nums[i]
            back *= nums[n - 1 - i]
            
            maxi = max(maxi, max(front, back))
        
        return maxi