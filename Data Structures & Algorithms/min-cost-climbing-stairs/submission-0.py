class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-1], 0

        for i in range(len(cost) - 2, -1, -1):
            tmp = one
            one = cost[i] + min(one, two)
            two = tmp
        
        return min(one, two)