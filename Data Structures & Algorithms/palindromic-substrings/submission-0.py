class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(s, l, r, count):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

            return count
        
        count = 0

        for i in range(len(s)):
            count = expand(s, i, i, count)
            count = expand(s, i, i + 1, count)
        
        return count

        