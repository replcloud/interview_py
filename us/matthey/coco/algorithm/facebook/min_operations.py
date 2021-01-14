import math
# Add any extra import statements you may need here
from collections import deque


# Add any helper functions you may need here


def minOperations(arr):
    # Write your code here
    L = len(arr)
    sarr = tuple(sorted(arr))

    def neighbors(narr):
        for i, x in enumerate(narr):
            if sarr[i] != x: break
        for j in range(i + 1, L):
            if narr[j] == sarr[i]:
                yield tuple(narr[:i]) + tuple([narr[j]]) + tuple(narr[i + 1:j]) + tuple([narr[i]]) + tuple(narr[j + 1:])

    q = deque([tuple(arr)])
    seen = {tuple(arr): 0}
    while q:
        curr = q.popleft()
        if curr == sarr: return seen[curr]
        for n in neighbors(curr):
            if n not in seen:
                seen[n] = seen[curr] + 1
                q.append(n)


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
