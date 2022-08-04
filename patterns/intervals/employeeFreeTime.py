"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        # Write your code here
        if not schedule:
            return []
        

        # break up intervals
        intervals = []

        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start,interval.end])
        
        intervals.sort(key=lambda x : x[0])

        res = []
        lastEnd = intervals[0][1]

        for i in range(1,len(intervals)):
            start = intervals[i][0]
            if start > lastEnd:
                res.append([Interval(lastEnd,start)])
            
            lastEnd = max(lastEnd,intervals[i][1])


        return res