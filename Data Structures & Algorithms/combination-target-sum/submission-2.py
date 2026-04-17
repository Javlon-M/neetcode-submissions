class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        nums.sort()

        def backtrack(i, path, s):
            if s == target:
                output.append(list(path))
                return
            
            for j in range(i, len(nums)):
                if s + nums[j] > target:
                    break

                backtrack(j, path + [nums[j]], s + nums[j])

        backtrack(0, [], 0)

        return output