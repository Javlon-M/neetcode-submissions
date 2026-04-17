class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def selectionSort(arr):
            n = len(arr)

            for i in range(n):
                minIdx = i 

                for j in range(i + 1, n):
                    if nums[j] < nums[minIdx]:
                        minIdx = j

                nums[i], nums[minIdx] = nums[minIdx], nums[i]
        
        selectionSort(nums)
        return nums

        