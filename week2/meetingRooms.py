class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:

        intervals.sort()

        for i in range(1, len(intervals)):

            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False

        return True
