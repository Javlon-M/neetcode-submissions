class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0

        l, r = 0, len(heights) - 1

        while r > l:
            a, b = heights[l], heights[r]
            
            maxi = max(maxi, min(a, b) * (r - l))

            if a < b:
                l += 1
            else:
                r -= 1

        return maxi