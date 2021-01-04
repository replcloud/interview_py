import math
# Add any extra import statements you may need here
from collections import Counter, defaultdict


# Add any helper functions you may need here

def min_length_substring(s, t):
    # Write your code here
    # Find the first substring
    # Deduct
    if len(s) < len(t): return -1
    minlen = -1
    b = -1
    e = -1
    target_counter = Counter(t)
    current_counter = Counter()
    extra_counter = Counter()
    hast = []
    i = 0
    while i < len(s):
        if s[i] in t:
            if b < 0:
                b = i
            hast.append(i)
            current_counter[s[i]] += 1
            if current_counter == target_counter:
                e = i
                minlen = e - b + 1
                break
        i += 1
    while i < len(s):
        if s[i] in t:
            hast.append(i)
            extra_counter[s[i]] += 1
            if s[b] in extra_counter:
                b = hast.pop(0)
                minlen = len(minlen, i - b + 1)
        i += 1
    if minlen != -1:
        return minlen
    else:
        return -1


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
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

# Add your own test cases here
