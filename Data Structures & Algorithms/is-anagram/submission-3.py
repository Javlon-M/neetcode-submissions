class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}

        for char in s:
            dic1[char] = dic1.get(char, 0) + 1
        
        for char in t:
            dic2[char] = dic2.get(char, 0) + 1
        
        if len(dic1) != len(dic2): return False

        for char in dic1:
            if dic1.get(char, 0) != dic2.get(char, 0): return False
        
        return True