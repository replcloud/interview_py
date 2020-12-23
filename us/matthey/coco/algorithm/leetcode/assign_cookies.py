from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cnt = 0
        g.sort()
        s.sort()
        j = 0

        for x in g:
            while j < len(s):
                if x <= s[j]:
                    cnt += 1
                    j += 1
                    break
                j += 1
        return cnt


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [3]
    print(Solution().findContentChildren(g, s))