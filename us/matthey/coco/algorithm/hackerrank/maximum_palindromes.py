#https://discuss.codechef.com/t/a-tutorial-on-fast-modulo-multiplication-exponential-squaring/2899
import math
from collections import Counter

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#
from datetime import datetime

gs = ''
factorial_l = [1]


def initialize(s):
    # This function is called once before all queries.
    global gs
    gs = s.strip()


#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def gen_factorial_cache(f):
    global factorial_l
    l = len(factorial_l)
    if l < f + 1:
        factorial_l += [-1] * (f + 1 - l)
        factorial_l[f] = math.factorial(f)
    if factorial_l[f] == -1:
        factorial_l[f] = math.factorial(f)
    return factorial_l[f]

def answerQuery(l, r):
    M = 10**9+7
    sumSame = 1
    odd_count = 0
    even_count = 0
    counter = Counter(gs[l - 1:r])
    for _, c in counter.items():
        sumSame *= gen_factorial_cache(c // 2)
        even_count += c // 2
        if c % 2 == 1:
            odd_count += 1
    res = math.factorial(even_count) // sumSame
    print(res)
    i = 0
    while res > 0:
        res >>= 2
        i += 1
    print(i)
    if odd_count > 0:
        if odd_count > M: odd_count = odd_count % M
        res = res * odd_count
        # res = gen_factorial_cache(even_count) // sumSame * odd_count
    else:
        # res = gen_factorial_cache(even_count) // sumSame
        pass
    return res % M

if __name__ == '__main__':
    # s = 'week'
    # print(answerQuery(2,3))
    with open('/Users/c/Downloads/input22.txt') as f:
        # s = 'wldsfubcsxrryqpqyqqxrlffumtuwymbybnpemdiwyqz'
        s = f.readline()
        n = int(f.readline())
        queries = []
        print(s)
        line = f.readline()
        while line:
            queries += tuple(map(int, line.strip().split())),
            line = f.readline()
        print(queries[0])
        initialize(s)
        s = datetime.now()
        print(answerQuery(queries[0][0], queries[0][1]))
        e = datetime.now()
        print(e-s)


        s = datetime.now()
        print(answerQuery(queries[0][0], queries[0][1]))
        e = datetime.now()
        print(e - s)
