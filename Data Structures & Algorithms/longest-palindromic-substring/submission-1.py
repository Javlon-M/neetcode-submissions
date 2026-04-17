class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def palindrome(i, j):
            l, r = i, j

            while 0 <= l and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            l += 1
            r -= 1
            
            return l, r - l + 1
        
        maxi, res = 0, 0
        for i in range(n):
            s1, leng1 = palindrome(i, i)
            s2, leng2 = palindrome(i, i + 1)

            if leng1 > maxi:
                res = s1
                maxi = leng1

            if leng2 > maxi:
                res = s2
                maxi = leng2
        
        return s[res: res + maxi]
        
        