from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        u = m * n - 1
        while l <= u:
            mid = l + (u - l) // 2
            print("{} {} {}".format(l, u, mid))
            r = mid // n
            c = mid % n
            print("{} {} {}".format(r, c, matrix[r][c]))
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                l = mid + 1
            else:
                u = mid - 1
        return False