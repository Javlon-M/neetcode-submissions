class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0 
        while i < len(nums2):
            nums1[m + i] = nums2[i]
            i += 1
        
        nums1.sort()
        return nums1
        