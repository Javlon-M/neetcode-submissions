class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            
            nums[abs(nums[i]) - 1] *= -1
            i += 1