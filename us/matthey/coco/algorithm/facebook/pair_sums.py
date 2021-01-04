import math
from collections import Counter

def numOfWays(arr, k):
    output = 0
    c = Counter(arr)
    addend2set = set()
    for x in c:
        if x in addend2set:
            continue
        if 2 * x == k:
            output += c[x] * (c[x] - 1) // 2
            addend2set.add(x)
            continue
        else:
            addend2 = k - x
            if addend2 in c:
                output += c[x] * c[addend2]
                addend2set.add(addend2)
    return output


if __name__ == '__main__':
    # input = [1, 2, 3, 4, 3]
    input = [1, 5, 3, 3, 3]
    print(numOfWays(input, 6))

'''
import math
# Add any extra import statements you may need here
from collections import Counter

# Add any helper functions you may need here


def numberOfWays(arr, k):
  # Write your code here
  output = 0
  c = Counter(arr)
  addendset = set()
  for x in c:
    if x in addendset:
      continue
    if 2 * x == k:
      output += c[x] * (c[x] - 1) // 2
      addendset.add(x)
      continue
    else:
      addend = k - x
      if addend in c:
        output += c[x] * c[addend]
        addendset.add(addend)
  return output












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
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
'''
