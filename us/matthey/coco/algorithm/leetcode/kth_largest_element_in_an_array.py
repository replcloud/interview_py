import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return min(heapq.nlargest(k, nums))

if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 3
    ans = Solution().findKthLargest(nums, k)
    print(ans)