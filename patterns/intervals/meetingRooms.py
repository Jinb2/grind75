class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda interval: interval.start)

        for i in range(1, len(intervals)):

            prevEnd = intervals[i - 1].end

            start = intervals[i].start

            if start < prevEnd:
                return False

        return True
