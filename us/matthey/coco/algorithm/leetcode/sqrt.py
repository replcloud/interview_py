class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l <= r:
            m = l + (r - l) // 2
            msq = m * m
            if msq <= x:
                l = m + 1
            else:
                r = m - 1

        return l - 1
