"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #[(0,30),(5,10),(15,20)]
        # 0,   5, 15
        # 10, 20, 30

        intervals.sort(key = lambda x : x.start)

        prev_start, prev_end = intervals[0].start, intervals[0].end
        for idx in range(1, len(intervals)):
            start, end = intervals[idx].start, intervals[idx].end
            if not (prev_end < start or end < prev_start):
                return False
        
        return True




