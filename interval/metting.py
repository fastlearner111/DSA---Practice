intervals = [(0,30),(5,10),(15,20)]
#Output: false

class Solution:
    def meeting_room(self, intervals):
        intervals.sort(key=lambda x:x[0])

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True