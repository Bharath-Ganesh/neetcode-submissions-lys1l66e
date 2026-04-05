"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals or len(intervals) == 0:
            return 0

        start_arr = []
        end_arr   = []
        for interval in intervals:
            start_arr.append(interval.start)
            end_arr.append(interval.end)

        start_arr.sort()
        end_arr.sort()
        idx1, idx2 = 0, 0
        n = len(intervals)
        max_meeting_room, meeting_room = 0, 0
        while idx1 <  n and idx2 < n:

            if start_arr[idx1] < end_arr[idx2]:
                meeting_room += 1
                idx1 += 1
            else:
                idx2 +=1
                meeting_room -= 1
            max_meeting_room = max(max_meeting_room, meeting_room)
        return max_meeting_room