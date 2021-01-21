from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = Counter(s)
        tc = Counter(t)
        extra = tc - sc
        return sum(extra.values())


if __name__ == '__main__':
    # s = "leetcode"
    # t = "practice"
    s = "gctcxyuluxjuxnsvmomavutrrfb"
    t = "qijrjrhqqjxjtprybrzpyfyqtzf"
    # s = "bab"
    # t = "aba"
    # s = "friend"
    # t = "family"
    print(Solution().minSteps(s, t))
