class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        l, r = 0, 0
        d = {}

        for r in range(len(s)):
            if s[r] in d:
                while l < d[s[r]]:
                    d.pop(s[l])
                    l += 1
                l = d[s[r]] + 1
            
            d[s[r]] = r

            maxi = max(maxi, r - l + 1)

        return maxi