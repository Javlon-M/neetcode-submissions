class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        # ends are less than from new start
        while i < n and intervals[i][1] < newInterval[0]: # 5 < 2 
            res.append(intervals[i])
            i += 1
        
        # starts are less than from new end
        while i < n and intervals[i][0] <= newInterval[1]: # 1 < 4
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
        
        