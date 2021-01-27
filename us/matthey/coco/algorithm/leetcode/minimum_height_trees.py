from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        neighbors = [set() for i in range(n)]

        for u, v in edges:
            print(u, v)
            neighbors[u].add(v)
            neighbors[v].add(u)

        leaves = []
        print(neighbors)
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            while leaves:
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves

    def findMinHeightTreesDFS(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs_helper(start, n):
            self.dist, self.parent = [-1] * n, [-1] * n
            self.dist[start] = 0
            dfs(start)
            return self.dist.index(max(self.dist))

        def dfs(start):
            for neib in neighbors[start]:
                if self.dist[neib] == -1:
                    self.dist[neib] = self.dist[start] + 1
                    self.parent[neib] = start
                    dfs(neib)

        neighbors = defaultdict(set)
        for u, v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        ind = dfs_helper(0, n)
        ind2 = dfs_helper(ind, n)

        path = []
        while ind2 != -1:
            path.append(ind2)
            ind2 = self.parent[ind2]
        Q = len(path)
        return list(set([path[Q // 2], path[(Q-1) // 2]]))


if __name__ == '__main__':
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    print(Solution().findMinHeightTreesDFS(n, edges))
