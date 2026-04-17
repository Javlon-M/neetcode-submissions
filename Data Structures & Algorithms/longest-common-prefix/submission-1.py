class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs, key=len)
        prefix = ""

        for i in range(len(mini)):
            for word in strs:
                if word[i] != mini[i]:
                    return mini[:i]
            
            prefix = mini[:i + 1]
        return prefix
            