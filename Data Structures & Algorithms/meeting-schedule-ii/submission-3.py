"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
[(0,40),(5,10),(15,20)]
        i1
0,   5, 15
10, 20, 40
i2
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n <= 1:
            return n
        startTime, endTime = [], []
        for interval in intervals:
            startTime.append(interval.start)
            endTime.append(interval.end)
        startTime.sort(key = lambda x : x)
        endTime.sort(key = lambda x : x)
        i1, i2 = 0, 0
        meeting_rooms = 0
        min_meeting_room = 0
        while i1 < n and i2 < n:
            if startTime[i1] < endTime[i2]:
                meeting_rooms += 1
                i1 += 1
            else:
                i2 -= 1
                meeting_rooms -= 1

            min_meeting_room = max(min_meeting_room, meeting_rooms)

        return min_meeting_room
