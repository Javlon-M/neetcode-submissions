class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini, maxi = 1, 1
        res = nums[0]
        
        for num in nums:
            temp = maxi * num

            maxi = max(num * maxi, num * mini, num)
            mini = min(temp, num * mini, num)

            res = max(res, maxi)

        return res