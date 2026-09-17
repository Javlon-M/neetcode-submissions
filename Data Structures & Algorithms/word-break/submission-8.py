class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}
        wordDict = set(wordDict)
        def dfs(i):
            if i in memo:
                return memo[i]

            word = ""

            for j in range(i, len(s)):
                word += s[j]
                if word in wordDict:
                    if dfs(j + 1):
                        return True

            memo[i] = False
            return False


        return dfs(0)