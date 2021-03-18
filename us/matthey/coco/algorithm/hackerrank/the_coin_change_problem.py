def getWays(n, c):
    # Write your code here
    c.sort()
    nc = len(c)
    res = [[1 if i == 0 else 0 for i in range(n + 1)] for _ in range(nc)]
    for i in range(1, n + 1):
        res[0][i] = 1 if (i % c[0]) == 0 else 0
    print(res)
    for i in range(1, nc):
        for j in range(1, n + 1):
            print('i=', i, 'j=', j)
            for k in range(j // c[i] + 1):
                res[i][j] += res[i-1][j - k * c[i]]
                print('i=', i, 'j=', j, 'k=', k, res)
    #
    return res[nc-1][n]

if __name__ == '__main__':
    n = 4
    c = [1, 2, 3]
    getWays(n, c)