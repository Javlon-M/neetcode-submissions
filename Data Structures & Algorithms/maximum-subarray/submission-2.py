class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, maxi = 0, nums[0]

        for num in nums:
            curr = max(curr + num, num)

            maxi = max(maxi, curr)
        
        return maxi