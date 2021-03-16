from collections import defaultdict


# Complete the countSort function below.
def countSort(arr):
    N = len(arr)
    NHALF = N // 2
    m = defaultdict(list)
    for i in range(N):
        idx, s = arr[i]
        if i < NHALF:
            arr[i] = (idx, '-')
        m[int(idx)] += i,
    # print(m)
    # print(sorted(m.keys()))
    # Remove nlogn sort
    # sorted_keys = sorted(m.keys())
    n_m = len(m)
    # print(max(m))
    for i in range(max(m) + 1):
        n_ks = len(m[i])
        for j in range(n_ks):
            # print("[i, j]", n_m - 1, n_ks - 1, i, j)
            if i == (max(m) + 1) and j == (n_ks - 1):
                print(arr[m[i][j]][1], end='')
            else:
                print(arr[m[i][j]][1], end=' ')


def countSortHelper(arr):
    d = defaultdict(list)
    h = len(arr) // 2
    for i, (x, y) in enumerate(arr):
        d[int(x)].append("-" if i < h else y)
    for i in range(max(d) + 1):
        for j in d[i]:
            yield j


def countSortCorrect(arr):
    print(*countSortHelper(arr))

def f():
    l = [1, 2, 3]
    for x in l:
        yield x

if __name__ == '__main__':
    # arr = []
    # with open('/Users/c/Downloads/input01.txt') as f:
    #     line_no = int(f.readline().strip())
    #     for i in range(line_no):
    #         line = f.readline().strip()
    #         l = line.strip().split()
    #         arr += [int(l[0]), l[1]],
    #
    # countSort(arr)
    print(*f())