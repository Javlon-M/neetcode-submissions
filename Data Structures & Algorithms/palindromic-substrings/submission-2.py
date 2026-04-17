class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def palindrome(count, i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1
                
            return count
            
        for i in range(n):
            count = palindrome(count, i, i)
            count = palindrome(count, i, i + 1) 
            

        return count