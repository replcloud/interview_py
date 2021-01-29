import heapq
import math
from collections import defaultdict
from typing import List


class Solution:
    def kClosestHeap(self, points: List[List[int]], K: int) -> List[List[int]]:
        d1 = {}
        d2 = defaultdict(list)
        for a, b in points:
            d1[(a, b)] = math.sqrt(pow(a, 2) + pow(b, 2))
            d2[math.sqrt(pow(a, 2) + pow(b, 2))].append([a, b])
        ksmallest = heapq.nsmallest(K, d1.values())
        ans = []
        for s in set(ksmallest):
            ans += d2[s]
        return ans

    def kClosestSortCustomKey(self, points, K):
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]

if __name__ == '__main__':
    points = [[1,3],[-2,2]]
    K = 1
    print(Solution().kClosest(points, K))
