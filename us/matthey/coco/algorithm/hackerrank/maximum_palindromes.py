#!/bin/python3
import math
from collections import Counter
import timeit

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

def gen_fs(n):
    global factorial_l
    i = len(factorial_l)
    while i < n:
        print(factorial_l)
        factorial_l += factorial_l[-1] * (i + 1),
        i += 1


def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    # gen_fs(5)
    # print(lst_fac)
    sumSame = 1
    odd_count = 0
    even_count = 0
    counter = Counter(gs[l - 1:r])
    for _, c in counter.items():
        sumSame *= math.factorial(c // 2)
        even_count += c // 2
        if c % 2 == 1:
            odd_count += 1
    res = math.factorial(even_count) // sumSame
    res = res if odd_count == 0 else res * odd_count
    return res

if __name__ == '__main__':
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
