#Given an array of intervals intervals where 
#intervals[i] = [start_i, end_i], return the minimum number
#of intervals you need to remove to make the rest of the 
#intervals non-overlapping.
#
#Note: Intervals are non-overlapping even if they have a 
#common point. For example, [1, 3] and [2, 4] are overlapping,
#but [1, 2] and [2, 3] are non-overlapping.
#
#Example 1:
intervals = [[1,2],[2,4],[1,4]]
#Output: 1
#Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.
#
#Example 2:
#Input: intervals = [[1,2],[2,4]]
#Output: 0

class Solution:
    def overlapping(self, intervals):
        intervals.sort(key = lambda x: x[1])

        removed = 0
        prev_end = intervals[0,1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < prev_end:
                removed += 1
            else:
                prev_end = end
                
        return removed  