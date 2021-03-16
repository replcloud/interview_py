"""/*
 * Given K lists that are already sorted and the total
 * number of elements in all the lists is N,
 * write a function that returns combined list with values sorted
 *
 * Example:
 *
 * a = [1, 4, 5, 8, 9]
 * b = [3, 4, 4, 6]
 * c = [0, 2, 8]

 * [0,1, 2, 3, 4, 4, 4, 5 ....]
 *

 res, a, b, c
      1  3  0
0     1  3  2
0 1   4  3  2
0 1 2 4  3  8

 sorted klogK
 minheap logk X

 (1, 0)

 */
"""
from collections import heapq, deque, defaultdict


def sortedList(int k, nums

):
# TODO: error checking
# K = 0, nums None
# K != 0, some of the arrays are empty
res = []
holder = defaultdict(tuple)
h = []
for i in range(k):
    holder = collections.deque(nums[i])  # for faster delete
    v1 = holder[i].remove()
    heapq.heappush(v, i)
while h:
    val, idx = heapq.heappop(h)
    res.append(val)
    # TODO: if not empty
    heapq.heappush((holder[idx], idx))
return res

###############

"""

Gregory1 gregory@fb.com gregory@gmail.com  
Coco coco@yahoo.com
Gregory2 gregory@gmail.com gregory@aol.com



Write a function that gets these emails list, and returns deduplicated

Coco ...
Gregory gregory@fb.com gregory@gmail.com gregory@aol.com
"""


def f(lines):
    # TODO: parse
    map = defaultdict(set)  # Name, set(emails)
    for line in lines:
        name, emails = parse(line)
        for email in emails:
            map[name].add(email)
    return map


"""
Subset

(gregory@fb.com gregory@gmail.com) + gregory@gmail.com gregory@aol.com
...
(coco@yahoo.com)


map: key quinque emails 

gregory@fb.com  (gregory@fb.com gregory@gmail.com) Gregory1
gregory@gmail.com (gregory@fb.com gregory@gmail.com) Gregory1\
coco@yahoo.com (coco@yahoo.com)

"""
