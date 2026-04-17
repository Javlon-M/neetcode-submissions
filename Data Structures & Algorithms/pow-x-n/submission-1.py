class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1

        def rec(tmp, p):
            if p == n:
                return tmp

            if n < 0:
                return rec(tmp * 1/x, p - 1)
            
            return rec(tmp * x, p + 1)

        return rec(1, 0)
        