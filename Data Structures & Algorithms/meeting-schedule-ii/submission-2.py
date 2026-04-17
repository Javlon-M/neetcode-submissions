"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start.sort()
        end.sort()

        count, maxi = 0, 0
        s, e = 0, 0

        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
                maxi = max(count, maxi)
            else:
                count -= 1
                e += 1
            
        return maxi