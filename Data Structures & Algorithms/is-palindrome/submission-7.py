class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.getStr(s)[::-1] == self.getStr(s)
    
    def getStr(self, s):
        strs = ""
        n = len(s)

        for i in range(n - 1, -1, -1):
            if not self.isChar(s[i]):
                continue

            strs += s[i]
        return strs.lower()
    
    def isChar(self, ch):
        return ch.isalnum()