class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b = float("inf"), 0
        ans = 0
        for p in prices:
            if a > p:
                a = p
                b = p
            elif b < p:
                b = p
                ans = max(ans, b - a)
        
        return ans