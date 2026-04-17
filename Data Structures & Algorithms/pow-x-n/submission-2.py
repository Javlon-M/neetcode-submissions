class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1

        def rec(tmp, p):
            if p == abs(n):
                return tmp

            return rec(tmp * x, p + 1)

        res = rec(1, 0)

        return res if n > 0 else 1 / res
        