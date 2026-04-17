class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxi = 0

        while r > l:
            a = r - l
            b = min(heights[l], heights[r])

            maxi = max(maxi, a * b)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxi

