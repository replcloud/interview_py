from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological Sorting
        indegree = [0 for _ in range(numCourses)]
        graph = defaultdict(set)
        order = []
        queue = []

        for c, p in prerequisites:
            indegree[c] += 1
            graph[p].add(c)

        for i in range(numCourses):
            if indegree[i] == 0:
                order.append(i)
                queue.append(i)

        while queue:
            cur = queue.pop(0)
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    order.append(next)
                    queue.append(next)

        return order if len(order) == numCourses else []

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0]]
    print(Solution().findOrder(numCourses, prerequisites))