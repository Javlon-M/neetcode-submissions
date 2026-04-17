class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxi = 0
        dic = {}
        for r in range(len(s)):
            if s[r] in dic:
                while l < dic[s[r]]:
                    dic.pop(s[l])
                    l += 1
                    
                l = dic[s[r]] + 1
            
            dic[s[r]] = r

            maxi = max(maxi, r - l + 1)
        
        return maxi