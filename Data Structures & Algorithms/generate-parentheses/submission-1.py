class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        OPEN, CLOSE = "(", ")"
        parents = []

        def dfs(left, right, path):
            if left < right or left > n:
                return

            if (len(path) == 2 * n and right == left):
                parents.append(path)
                return

            dfs(left + 1, right, path + OPEN)
            dfs(left, right + 1, path + CLOSE)
        
        dfs(0, 0, "")

        return parents