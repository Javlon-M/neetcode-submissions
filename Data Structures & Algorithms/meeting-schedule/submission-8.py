"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        inters = []
        for inter in intervals:
            inters.append((inter.start, inter.end))
        
        sorted(inters)

        a, b = inters[0]
        for i in range(1, len(intervals)):
            c, d = inters[i]
            if a <= c < b or c < b <= d:
                return False
            
            a, b = c, d
        
        return True
