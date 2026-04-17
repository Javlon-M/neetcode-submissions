class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def do(count, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

            l += 1
            return count
        
        for i in range(len(s)):
            count = do(count, i, i)
            count = do(count, i, i + 1)

        return count