from collections import defaultdict


def answerQueries(queries, N):
    ans = []
    h = defaultdict(int)
    for q, idx in queries:
        if q == 1 and idx <= N:  # SET
            for j in range(1, idx + 1):
                h[j] = max(h[j], idx)
        elif q == 2:  # GET
            ans.append(h[idx]) if h[idx] > 0 else ans.append(-1)
    return ans

def answerQueriesSet(queries, N):
    ans = []
    h = defaultdict(set)
    for q, idx in queries:
        if q == 1 and idx <= N:  # SET
            for j in range(1, idx + 1):
                h[j].add(idx)
        elif q == 2:  # GET
            if len(h[idx]) > 0:
                ans.append(min(h[idx]))
            else:
                ans.append(-1)
    return ans


if __name__ == '__main__':
    N = 5
    Q = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2], [2, 1]]

    print(answerQueries(Q, N))
