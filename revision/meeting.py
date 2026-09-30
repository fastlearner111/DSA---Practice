class Solution:
    def meeting(self, intervals):
        intervals.sort(key = lambda x: x[0])

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True