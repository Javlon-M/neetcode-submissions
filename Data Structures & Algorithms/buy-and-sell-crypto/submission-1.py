class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, maxi = float("inf"), float("-inf")
        profit = 0

        for price in prices:
            if price < mini:
                mini = price
                maxi = price
            elif price > maxi:
                maxi = price
                profit = max(maxi - mini, profit)

        return profit