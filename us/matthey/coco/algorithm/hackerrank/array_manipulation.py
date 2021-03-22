from operator import itemgetter


def arrayManipulation(n, queries):
    mx = 0
    ac = 0
    l = []
    for a, b, k in queries:
        l += (a, k),
        l += (b, -k),
    l = sorted(sorted(l, key=itemgetter(1), reverse=True), key=itemgetter(0))
    print(l)
    for a, k in l:
        ac += k
        print(a, k, ac)
        mx = max(ac, mx)
    return mx


if __name__ == '__main__':
    n = 5
    queries = ((1, 2, 100),
               (2, 5, 100),
               (3, 4, 100))
    arrayManipulation(n, queries)
