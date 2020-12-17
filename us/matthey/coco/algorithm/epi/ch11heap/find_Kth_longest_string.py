import heapq
from typing import List


def find_kth_longest_string(L: List[int], k: int) -> List[int]:
    heapq.heapify(L)
    # return [heapq.heappop(L) for i in range(min(k, len(L)))]
    return heapq.nlargest(k, L)


if __name__ == '__main__':
    L = [2, 7, 4, 1, 8, 1, 6, 3, 5]
    res = find_kth_longest_string(L, 3)
    print(res)

