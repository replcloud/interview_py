from typing import List


class MonotonicArray:
    def isMonotonic(self, A: List[int]) -> bool:
        l = len(A)
        if l == 1:
            return True
        proIncrease = True if A[-1] - A[0] > 0 else False
        if proIncrease:
            for i in range(1, l):
                if A[i] < A[i - 1]:
                    return False
        else:
            for i in range(1, l):
                if A[i] > A[i - 1]:
                    return False
        return True
