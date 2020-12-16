import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        reversed_stones = [-x for x in stones]
        heapq.heapify(reversed_stones)
        while len(reversed_stones) > 1:
            heaviest = heapq.heappop(reversed_stones)
            second_heaviest = heapq.heappop(reversed_stones)
            if heaviest != second_heaviest:
                heapq.heappush(reversed_stones, heaviest - second_heaviest)
        if len(reversed_stones) > 0:
            return -reversed_stones[0]
        else:
            return 0

    def lastStoneWeight2(self, A):
        h = [-x for x in A]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]