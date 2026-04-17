class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(ints, path):
            if len(path) == len(nums):
                output.append(list(path))
                return
            
            for i in range(len(ints)):
                backtrack(ints[:i] + ints[(i + 1):], path + [ints[i]])
                

        backtrack(nums, [])

        return output