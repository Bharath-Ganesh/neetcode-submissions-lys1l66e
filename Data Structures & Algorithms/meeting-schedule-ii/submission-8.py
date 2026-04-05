"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
            intervals = [(0,40),(5,10),(15,20)]
            start = 0,  5,  15
            end.  = 10, 20, 40
        """
        start, end = [], []
        for interval in intervals:
            start.append(interval.start)      
            end.append(interval.end) 
        start.sort()
        end.sort()
        n = len(start)
        idx1, idx2, meeting_room, max_meeting_rooms = 0, 0, 0, 0

        while idx1 < n and idx2 < n:
            if start[idx1] < end[idx2]:
                meeting_room += 1
                idx1 += 1
            else:
                meeting_room -= 1
                idx2 += 1                
            max_meeting_rooms = max(max_meeting_rooms, meeting_room)
        return max_meeting_rooms







