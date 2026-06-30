"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n         = len(intervals)
        start_arr = []
        end_arr   = []
        for interval in intervals:
            start_arr.append(interval.start)
            end_arr.append(interval.end)
        
        start_arr.sort()
        end_arr.sort()
        i1, i2 = 0, 0
        meeting_rooms = 0
        max_meeting_rooms = 0
        while i1 < n and i2 < n:
            if start_arr[i1] < end_arr[i2]:
                i1 += 1
                meeting_rooms += 1
            else:
                i2 += 1 
                meeting_rooms -= 1
            max_meeting_rooms = max(meeting_rooms, max_meeting_rooms)
        return max_meeting_rooms



        