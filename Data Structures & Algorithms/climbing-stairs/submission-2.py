class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2 = 0, 1

        i = 0
        while i < n:
            tmp = s1 + s2
            s1 = s2
            s2 = tmp

            i += 1
        
        return s2