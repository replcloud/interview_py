import heapq
from typing import List

"""
[[1,5,9],
[10,11,13],
[12,13,15]]

loop k times
h = [1,5,9]
i = 0 pop 1 from row 0 refill heap with row 0 matrix[0][1]
i = 1 pop 5 from row 1 refill heap with row 1 matrix[1][1]
i = 2 pop 9 from row 1 refill heap with row 1 matrix[1][2]
...
i = k - 1

1 0 0
5 0 1
9 0 2
10 1 0
11 1 1
12 2 0
13 1 2
13 2 1

"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        n = len(matrix)
        for i in range(n):
            heapq.heappush(h, (matrix[0][i], 0, i))
        for i in range(k):
            v, r, c = heapq.heappop(h)
            if r < n - 1:
                heapq.heappush(h, (matrix[r + 1][c], r + 1, c))
        return v