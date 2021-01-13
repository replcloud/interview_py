from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        being_trusted_map = defaultdict(set)
        for i in range(1, N + 1):
            being_trusted_map[i] = set()
        trusting = set()
        for pair in trust:
            trusting.add(pair[0])
            being_trusted_map[pair[1]].add(pair[0])
        town_judge_prospectives = set(being_trusted_map.keys()) - trusting
        count = 0
        town_judge = None
        for x in town_judge_prospectives:
            if len(being_trusted_map[x]) != N - 1:
                continue
            count += 1
            town_judge = x

        if count == 1:
            return town_judge
        else:
            return -1

    def findJudge_graph_count_in_out(self, N, trust):
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

    def findJudge_26pt(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0: return 1

        ruleout = defaultdict(bool)
        trustcount = defaultdict(set)

        for t in trust:
            ruleout[t[0]] = True
            trustcount[t[1]].add(t[0])

        for k, v in trustcount.items():
            if len(v) == N - 1 and ruleout[k] is False:
                return k
        return -1
