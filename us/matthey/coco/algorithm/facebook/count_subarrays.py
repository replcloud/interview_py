def count_subarrays(arr):
    L = []
    R = []
    L.append(1)
    closest_peak = arr[0]
    peaks = []
    peak_location = {}
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            for p in peaks[::-1]:
                if p > arr[i]:
                    closest_peak = p
                    break
            if closest_peak > arr[i]:
                L.append(i - peak_location[closest_peak])
            else:
                L.append(i + 1)
        else: #if arr[i] < arr[i - 1]
            L.append(1)
            peaks.append(arr[i - 1])
            peak_location[arr[i - 1]] = i - 1
    R.insert(0, 1)
    closest_peak = arr[-1]
    # It's dulicate of peaks
    peaks = []
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            for p in peaks:
                if p > arr[i]:
                    closest_peak = p
                    break
            if closest_peak > arr[i]:
                R.insert(0, peak_location[closest_peak] - i)
            else:
                R.insert(0, len(arr) - i)
        else:
            R.insert(0, 1)
            peaks.insert(0, arr[i + 1])
    print(R)
    print(L)
    res = []
    for i in range(len(R)):
        res.append(R[i] + L[i] - 1)
    return res

if __name__ == '__main__':
    input1 = [3, 4, 1, 6, 2]
    output1 = [1, 3, 1, 5, 1]
    input2 = [2, 4, 7, 1, 5, 3]
    output2 = [1, 2, 6, 1, 3, 1]
    print(count_subarrays(input2))
'''
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def count_subarrays(arr):
  # Write your code here
  L = []
  R = []
  res = []
  L.append(1)
  closest_peak = arr[0]
  peaks = []
  peak_location = {}
  for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
      for p in peaks[::-1]:
        if p > arr[i]:
          closest_peak = p
          break
      if closest_peak > arr[i]:    
        L.append(i - peak_location[closest_peak])
      else:
        L.append(i + 1)
    else:
      L.append(1)
      peaks.append(arr[i - 1])
      peak_location[arr[i - 1]] = i - 1
  R.insert(0, 1)
  peaks = []
  closest_peak = arr[-1]
  for i in range(len(arr) - 2, -1, -1):
    if arr[i] > arr[i + 1]:
      for p in peaks:
        if p > arr[i]:
          closest_peak = p
          break
      if closest_peak > arr[i]:
        R.insert(0, peak_location[closest_peak] - i)
      else:
        R.insert(0, len(arr) - i)
    else:
      peaks.insert(0, arr[i + 1])
      R.insert(0, 1)
  print(L)
  print(R)
  for i in range(len(R)):
    res.append(L[i] + R[i] - 1)
  return res
      
	









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
'''