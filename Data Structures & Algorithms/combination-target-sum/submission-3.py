class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def backtrack(i, com):
            s = sum(com)
            if s == target:
                output.append(list(com))
                return
            
            if s > target or i > len(nums):
                return
            
            for j in range(i, len(nums)):
                backtrack(j, com + [nums[j]])
            

        backtrack(0, [])
        return output