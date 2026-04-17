class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        n = len(intervals)
        i = n - 1
        while i > 0:
            a, b = intervals[i][0], intervals[i][1] # 2, 5
            c, d = intervals[i - 1][0], intervals[i - 1][1] # 1, 5
            if a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d:
                intervals[i - 1][0], intervals[i - 1][1] = min(a, c), max(b, d) 
                del intervals[i]
            else:
                intervals[i][0], intervals[i][1] = max(a, c), max(b, d)
                intervals[i - 1][0], intervals[i - 1][1] = min(a, c), min(b, d)

            i -= 1

        return intervals