class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, path, total):
            if target == total:
                res.append(list(path))
                return
            

            for j in range(i, len(nums)):
                if target >= total + nums[j]:
                    dfs(j, path + [nums[j]], total + nums[j])

        dfs(0, [], 0)

        return res