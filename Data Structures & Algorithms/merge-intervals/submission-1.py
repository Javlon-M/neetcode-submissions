class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        i = 1
        while i < len(intervals):
            a, b = intervals[i - 1]
            c, d = intervals[i]

            if b < c: 
                i += 1
                continue

            intervals[i - 1][0] = min(a, c)
            intervals[i - 1][1] = max(b, d)
            del intervals[i]

        return intervals

