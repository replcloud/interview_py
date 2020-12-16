import heapq
from typing import List


class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = nums
    #     heapq.heapify(self.nums)
    #
    # def add(self, val: int) -> int:
    #     heapq.heappush(self.nums, val)
    #     return heapq.nlargest(self.k, self.nums)

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)
        while len(self.h) > k:
            heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        heapq.heappushpop(self.h, val)
        return self.h[0]

if __name__ == '__main__':
    k = KthLargest(3, [4,5,8,2])
    print(k.add(3))
    print(k.add(5))
    print(k.add(10))
    print(k.add(9))
    print(k.add(4))