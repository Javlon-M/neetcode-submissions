class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, leng = "", 0

        def do(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            return s[l:r]
        
        for i in range(len(s)):
            r1 = do(i, i)
            r2 = do(i, i + 1)

            if leng < len(r1):
                leng = len(r1)
                res = r1

            if leng < len(r2):
                leng = len(r2)
                res = r2

        return res