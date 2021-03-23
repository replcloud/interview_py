#!/bin/python3

import os
import sys
import heapq
#
# Complete the runningMedian function below.
#
def runningMedianSlow(a):
    #
    # Write your code here.
    #
    minh = []
    maxh = []
    res = []
    for x in a:
        if len(minh) == 0:
            heapq.heappush(minh, x)
        else:
            if x >= minh[0]:
                heapq.heappush(minh, x)
            else:
                heapq.heappush(maxh, -x)
            if len(minh) > len(maxh) + 1:
                heapq.heappush(maxh, -heapq.heappop(minh))
            elif len(minh) < len(maxh):
                heapq.heappush(minh, -heapq.heappop(maxh))
        res += ((minh[0] - maxh[0]) / 2) if len(minh) == len(maxh) else minh[0],
    return res

if __name__ == '__main__':
    a = []
    a = [x for x in range(1, 11)]
    # with open('/Users/c/Downloads/input01.txt') as f:
    #     n = int(f.readline())
    #     line = f.readline()
    #     while line:
    #         a += int(line),
    #         line = f.readline()
    output = runningMedian(a)
    # for x in a:
    #     print(x)
    print(output)
