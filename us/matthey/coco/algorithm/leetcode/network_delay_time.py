import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTimeSlow(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        for s, d, t in times:
            graph[d].add(((s, t)))

        def dfs(self, source, depth, visited):
            visited.add(source)
            if source == k:
                return depth
            res = []
            for s, t in graph[source]:
                if s not in visited:
                    res.append(dfs(self, s, depth + t, set(visited)))
            if res and -1 not in res: return min(res)
            return -1

        res = []
        for i in range(1, n + 1):
            if i != k:
                res.append(dfs(self, i, 0, set()))
        return -1 if -1 in res else max(res)

    def networkDelayTimeDFS(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        dist = {node: float('inf') for node in range(1, n + 1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(k, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    def networkDelayTimeDijkstra(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, n)}
        seen = [False] * (n + 1)
        dist[k] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, n + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei]), dist[cand_node + d]
        ans = max(dist.values())
        return ans if ans < float('inf') else -1

    def networkDelayTimeHeap(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, k)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))
        return max(dist.values()) if len(dist) == n else -1

if __name__ == '__main__':
    # times = [[2,1,1],[2,3,1],[3,4,1]]
    times = [[1, 2, 1], [2, 3, 2], [1, 3, 2]]
    # n = 4
    # k = 2
    n = 3
    k = 1
    print(Solution().networkDelayTime(times, n, k))
