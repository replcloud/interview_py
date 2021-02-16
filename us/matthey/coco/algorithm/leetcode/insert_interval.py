from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
                continue
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                res += intervals[i:]
                break
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        if len(res) == 0:
            return [newInterval]
        elif res[-1][1] < newInterval[0]:
            res.append(newInterval)
        return res
