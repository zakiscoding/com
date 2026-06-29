"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        res = []
        for meeting in intervals:
            if res and meeting.start>=res[0]:
                heapq.heappop(res)
            heapq.heappush(res, meeting.end)
        return len(res)