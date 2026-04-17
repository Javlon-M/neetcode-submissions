class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        l = len(nums)
        k = k % l

        reverse(nums, 0, l - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, l - 1)

        return nums

        
        