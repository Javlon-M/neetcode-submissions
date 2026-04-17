class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, n = len(nums), len(nums)
        
        i = 0
        while i < k:
            if nums[i] == val:
                del nums[i]
                k -= 1
            else:
                i += 1

        return k