class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        s1 = sorted(s1)
        i, j = l1, 0
        while i <= l2:
            a = sorted(s2[j:i])

            if s1 == a:
                return True
            i += 1
            j += 1
        
        return False
        
