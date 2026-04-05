"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        """
            3......5                                                    40......50   
                        8.........12                    25.........60
                                    15.........20
                            10...................................30
        """

        prev_start, prev_end = intervals[0].start, intervals[0].end
        meeting_rooms = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if not (prev_start > end or prev_end < start):
                return False
        return True