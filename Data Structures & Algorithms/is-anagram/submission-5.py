class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}

        for char in s:
            dic1[char] = dic1.get(char, 0) + 1
        
        for char in t:
            dic1[char] = dic1.get(char, 0) - 1
        
        for char in dic1:
            if dic1[char] != 0: return False

        return True