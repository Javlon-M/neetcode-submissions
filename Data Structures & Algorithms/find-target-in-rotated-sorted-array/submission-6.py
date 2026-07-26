class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r > l:
            m = (r + l)//2
            if nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m
        pivot = l
    
        def binary_search(l, r):
            while r >= l:
                m = (r + l)//2

                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

            return -1

        res = binary_search(0, pivot - 1)

        if res != -1:
            return res
        
        return binary_search(pivot, len(nums) - 1)


