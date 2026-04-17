class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()

        def backtract(i, path, pathSum):
            if pathSum == target:
                output.append(list(path))
                return
            
            prev = -1
            for j in range(i, len(candidates)):
                if pathSum + candidates[j] > target or prev == candidates[j]:
                    continue
                backtract(j + 1, path + [candidates[j]], pathSum + candidates[j])
                prev = candidates[j]

        backtract(0, [], 0)

        return output