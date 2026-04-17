class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] == nums[i - 1] and nums[i] != None:
                del nums[i]
                nums.append(None)
                i -= 1
            i += 1
        
        return n - nums.count(None)