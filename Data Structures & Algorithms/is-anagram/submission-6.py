class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 != n2: return False

        countS, countT = {}, {}

        for i in range(n1):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
            
        return countS == countT