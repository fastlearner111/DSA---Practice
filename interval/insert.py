#Example 1:
#intervals = [[1,3],[4,6]]
#newInterval = [2,5]
#
#Output: [[1,6]]
#Explanation: [2,5] overlaps with [1,3] and [4,6], so all three are merged into [1,6].
#
#Example 2:
intervals = [[1,2],[3,5],[9,10]]
newInterval = [6,7]
#Output: [[1,2],[3,5],[6,7],[9,10]]


class Solution:
    def insert_interval(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = min(newInterval[0], intervals[i][0])
            newInterval = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1
        return result
