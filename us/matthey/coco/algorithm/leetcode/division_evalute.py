from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            u, v = equations[i]
            graph[u][v] = values[i]
            graph[v][u] = 1 / values[i]
        print(graph)
        res = []

        def get_weight(s: str, e: str, visited: set):
            if s not in graph:
                return -1
            if e in graph.get(s):
                return graph.get(s).get(e)
            visited.add(s)
            for next in graph.get(s):
                if next not in visited:
                    weight = get_weight(next, e, visited)
                    if weight != -1:
                        return graph.get(s).get(next) * weight
            return -1

        for s, e in queries:
            res.append(get_weight(s, e, set()))
        return res

if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    quries = [["a", "c"]]
    # quries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(Solution().calcEquation(equations, values, quries))
