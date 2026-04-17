class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        memo = set()
        
        def dfs(amount, path):
            if amount == 0:
                path.sort()
                if path not in res:
                    res.append(path.copy())
                return
            
            # if amount in memo: return

            for num in nums:
                if amount >= num:
                    dfs(amount - num, path + [num])
            
            # memo.add(amount)

        dfs(target, [])

        return res