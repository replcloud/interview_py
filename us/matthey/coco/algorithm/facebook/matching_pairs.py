import math
# Add any extra import statements you may need here
from collections import defaultdict


# Add any helper functions you may need here


def matching_pairs(s, t):
    # Write your code here
    N = len(s)
    swapped = 0
    mp = {}
    for i in range(N):
        if s[i] != t[i]:
            if s[i] in mp and swapped == 0:
                swapped = 1
            mp[t[i]] = i
    unmatched_count = len(mp)
    if unmatched_count == 0:
        return N - 2
    else:
        return N - unmatched_count if swapped == 0 else N - unmatched_count + 2


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
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here
