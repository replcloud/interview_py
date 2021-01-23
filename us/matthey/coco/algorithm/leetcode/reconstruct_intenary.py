from collections import defaultdict, deque
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for dept, dest in tickets:
            graph[dept].append((dept, dest))

        L = len(tickets)
        if L == 0: return []
        if "JFK" not in graph: return []
        res = []

        def findpath(s: str, visited: set):
            if len(visited) == L: return [s]
            if s not in graph: return []
            for dept, dest in sorted(graph[s]):
                if (dept, dest) not in visited:
                    visited.add((dept, dest))
                    path = findpath(dest, visited)
                    if path:
                        return [s] + path
                    else:
                        visited.remove((dept, dest))
            return []

        return res + findpath("JFK", set())

    def findItineraryRecursive(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]

    def findItineraryIterative(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
            print(b,)
            print(b)
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]


if __name__ == '__main__':
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    # tickets = [["MUC", "JFK"], ["JFK", "MUC"]]
    # tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    # tickets = [["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], ["ANU", "EZE"], ["TIA", "ANU"],
    #            ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]]
    print(Solution().findItineraryIterative(tickets))
