#Given an array of intervals where intervals[i] = [start_i, end_i],
#merge all overlapping intervals, and return an array of the non-overlapping
#intervals that cover all the intervals in the input.
#
#You may return the answer in any order.
#
#Note: Intervals are non-overlapping if they have no common point.
#  For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

#Example 1:
#intervals = [[1,3],[1,5],[6,7]]
#Output: [[1,5],[6,7]]


#Example 2:
intervals = [[1,2],[2,3]]
#Output[[1,3]]

class Solution:
    def interval_merge(self, intervals):
        intervals.sort(key = lambda x: x[0])
        merged = []
    
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
    
        return merged