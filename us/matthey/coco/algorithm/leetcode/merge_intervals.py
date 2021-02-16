from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                e = res.pop()
                res.append([min(e[0], intervals[i][0]), max(e[1], intervals[i][1])])
            else:
                res.append(intervals[i])
        return res
