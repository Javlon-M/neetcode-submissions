class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        n = len(intervals)
        i = 1
        while i < n:
            if res[-1][1] >= intervals[i][0]:
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])

            i += 1
        
        return res
