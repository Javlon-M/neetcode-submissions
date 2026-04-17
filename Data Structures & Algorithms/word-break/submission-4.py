class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo: 
                return memo[i]
            
            word = ""
            for j in range(i, len(s)):
                word += s[j]

                if word in wordDict:
                    ans = dfs(j + 1)
                    if ans: return True
            
            memo[i] = False
            return False
        
        return dfs(0)