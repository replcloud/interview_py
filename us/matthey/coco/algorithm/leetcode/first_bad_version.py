import random


def isBadVersion(version):
    target = random.randint(0, 99)
    return version >= target


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            m = l + (r - l) // 2
            if isBadVersion(m) == True:
                r = m - 1
            else:
                l = m + 1
        return l
