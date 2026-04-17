class Solution:
    def reverse(self, x: int) -> int:
        org = x
        x = abs(x)
        x = int(str(x)[::-1])

        if org < 0: x *= -1

        if not (-2**31 <= x <= 2**31 - 1): return 0

        return x

