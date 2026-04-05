"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        if n <= 1:
            return True
        
        intervals.sort(key = lambda x: x.start)
        prev_start, prev_end = intervals[0].start, intervals[0].end
        for i in range(1, n):
            start, end = intervals[i].start, intervals[i].end
            if prev_end > start:
                return False
            prev_start, prev_end = start, end   
        return True
