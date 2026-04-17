class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordDict = set(wordDict)
        
        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo: 
                return memo[i]
            
            word = ""
            for j in range(i, len(s)):
                word += s[j]
                if word in wordDict:
                    res = dfs(j + 1)

                    if res:
                        return True
                    
                    memo[i] = res

            return False
        return dfs(0)