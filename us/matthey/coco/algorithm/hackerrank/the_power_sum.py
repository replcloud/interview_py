import math


def powerSum(X, N):
    def findLargestH(x):
        h = int(math.sqrt(x))
        while x >= int(math.pow(h, N)):
            break
            h -= 1
        return h

    def helper(x, h):
        if h == 0:
            return 1 if x == 0 else 0
        c = 0
        return helper(x, h - 1) + (helper(x - int(math.pow(h, N)), h - 1) if x >= int(math.pow(h, N)) else 0)

    return helper(X, findLargestH(X))

if __name__ == '__main__':
    X = 10
    N = 2
    print(powerSum(X, N))