"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        intervals = sorted(intervals, key=lambda x: x.start)

        temp = intervals[0]

        for i in range(1, len(intervals)):
            intrvl = intervals[i]
            a, b = temp.start, temp.end
            c, d = intrvl.start, intrvl.end

            if a <= c < b: return False

            temp.start, temp.end = c, d
        
        return True