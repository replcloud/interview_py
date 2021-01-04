import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def isBalanced(s):
    # Write your code here
    bracket_table = {')': '(', '}': '{', ']': '['}
    close_brakets = bracket_table.keys()
    open_brakets = bracket_table.values()
    if s and len(s) == 0: return True
    st = []
    for c in s:
        if c in open_brakets:
            st.append(c)
        elif c in close_brakets:
            if bracket_table[c] == st[-1]:
                st.pop()
            else:
                return False
        else:
            return False
    return True if len(st) == 0 else False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


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
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "{[(])}"
    expected_1 = False
    output_1 = isBalanced(s1)
    check(expected_1, output_1)

    s2 = "{{[[(())]]}}"
    expected_2 = True
    output_2 = isBalanced(s2)
    check(expected_2, output_2)

    # Add your own test cases here
