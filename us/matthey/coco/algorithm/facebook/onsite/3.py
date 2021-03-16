"""
Problem 1: Convert a sorted integer array into a binary min heap


Example input:
[1, 2, 5, 7, 12, 30, 31]

output:
      1
  2     5
7  12  30  31

// function to implement
Node heapify(int[] orderedList);

class Node {
   Node left;
   Node right;
   int val;
}


1

2 5

7 12 30 31

"""
from collections import deque
def convert(arr):
    if not arr: return None
    q = deque()
    root = Node(arr[0])
    q.append(root)
    for i in range(1, len(arr), 2):
        e = q[0]
        e.left = Node(arr[i])
        if i + 1 <= len(arr) - 1:
            e.right = Node(arr[i + 1])
        q.popleft()
    return root

"""""
Normal postive test case ex. 
Emtpy arr
arr [1, 1, 1]
arr length is odd
arr length is even 
large arr size

Time: outco(n)
Space: outco(n)
"""""

"""""
Problem 2: Maximum Subarray Product

Given a one dimensional array that may contain both zeros, positive and negative integers, find the maximum product of a contiguous subarray of this array.

Example:
[-1, 0, -6, 5, -2, 1, -6]
60 [-6, 5, -2], [-6, 5, -2, 1]

// function to implement
int maxSubarrayProduct(int[] nums);


"""""
[0, 0], [0, 1] ..[0, len(arr)]
[1, 1] ...[1, len(arr)]

Walk L - > R [-1, 0, 0, 0, 0, 0, 0]
Walk R - > L [0 0 -360 60 12 -6 -6]















