def rotationCipher(input, rotationFactor):
    output = ''
    for x in input:
        if not x.isalnum():
            output += x
        elif x.isdigit():
            output += chr(ord('0') + ((ord(x) - ord('0') + rotationFactor) % 10))
        elif x.isalpha() and x.isupper():
            output += chr(ord('A') + ((ord(x) - ord('A') + rotationFactor) % 26))
        elif x.isalpha() and x.islower():
            output += chr(ord('a') + ((ord(x) - ord('a') + rotationFactor) % 26))
    return output

if __name__ == '__main__':
    input = 'Aa:@123'
    print(rotationCipher(input, 3))

'''
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
  # Write your code here
  output = ''
  for c in input:
    if not c.isalnum():
      output += c
    elif c.isdigit():
      output += chr(ord('0') + (ord(c) - ord('0') + rotation_factor) % 10)
    elif c.isalpha() and c.isupper():
      output += chr(ord('A') + (ord(c) - ord('A') + rotation_factor) % 26)
    elif c.isalpha() and c.islower():
      output += chr(ord('a') + (ord(c) - ord('a') + rotation_factor) % 26)
  return output











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
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
'''