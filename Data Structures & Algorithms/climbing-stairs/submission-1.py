"""
1 + 1
2

1 + 1 + 1
2 + 1
1 + 2

1 + 1 + 1 + 1
2 + 1 + 1
1 + 2 + 1
1 + 1 + 2
2 + 2

1 + 1 + 1 + 1 + 1
2 + 1 + 1 + 1
1 + 2 + 1 + 1
1 + 1 + 2 + 1
1 + 1 + 1 + 2
2 + 2 + 1
2 + 1 + 2
1 + 2 + 2

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        m1, m2 = 1, 1

        for _ in range(1, n):
            m1, m2 = m2, m1 + m2
        
        return m2










