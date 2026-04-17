"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        temp = set()

        for i in range(len(intervals)):
            intrvl = intervals[i]
            a, b = intrvl.start, intrvl.end

            if a in temp or b in temp: return False

            for i in range(a, b):
                temp.add(i)
        
        return True