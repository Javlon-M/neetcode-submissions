class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        c, d = newInterval
        temp, isInserted = [], False
        for a, b in intervals:
            if a >= c and not isInserted:
                temp.append([c, d])
                isInserted = True
            temp.append([a, b])

        if len(temp) == len(intervals):
            temp.append([c, d])
        
        i = 1
        while i < len(temp):
            a, b = temp[i - 1]
            c, d = temp[i]

            if a <= c <= b <= d:
                temp[i - 1] = [a, d]
                del temp[i]
                i -= 1
            elif a <= c <= d <= b:
                temp[i - 1] = [a, b]
                del temp[i]
                i -= 1
            i += 1

        return temp



