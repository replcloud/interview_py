import collections


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def neighbors(S):
            for i, c in enumerate(S):
                if c != B[i]:
                    break

            T = list(S)
            for j in range(i+1, len(S)):
                if S[j] == B[i]:
                    yield S[:i] + S[j] + S[i+1:j] + S[i] + S[j+1:]
                    # T[i], T[j] = T[j], T[i]
                    # yield "".join(T)
                    # T[j], T[i] = T[i], T[j]

        queue = collections.deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbors(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)

    def kSimilarityGreedy(self, A: str, B: str) -> int:
        # Greedy algorithm is not an optimized answer
        if A == B: return 0

        queue = collections.deque([A])
        visited = set([A])
        step = -1

        while queue:
            n = len(queue)
            step += 1

            while n > 0:
                s = queue.popleft()
                n -= 1

                for i in range(len(B)):
                    if s[i] != B[i]:
                        break

                for j in range(i + 1, len(B)):
                    if s[j] == B[i]:
                        s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                        if s == B:
                            return step + 1
                        if s not in visited:
                            queue.append(s)
                            visited.add(s)

        return -1


if __name__ == '__main__':
    A = "abccaacceecdeea"
    B = "bcaacceeccdeaae"
    print(Solution().kSimilarity(A, B))
