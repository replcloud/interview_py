
from collections import deque

# Complete the highestValuePalindrome function below.
# TODO: index replace popleft
def highestValuePalindrome(s, n, k):
    # print(s, n, k)
    arr = list(s)
    diff = []
    for i in range(n // 2):
        # print(i, arr[i], (n - 1 - i), arr[n - 1 - i])
        if (arr[i] != arr[n - 1 - i]):
            diff += i,
    n_d = len(diff)
    n_ex = k - n_d
    i_diff = 0
    # print(arr, diff, n_d, n_ex)
    if n_ex < 0:
        return '-1'
        # return -1
    for i in range(n // 2):
        if n_ex >= 2:
            if i_diff < n_d and i == diff[i_diff]:
                if arr[i] != '9' and arr[n - 1 - i] != '9':
                    arr[i] = '9'
                    arr[n - 1 - i] = '9'
                    n_ex -= 1
                    # n_d -= 1
                else:
                    arr[i] = '9'
                    arr[n - 1 - i] = '9'
                i_diff += 1
            else:
                if arr[i] != '9':
                    arr[i] = '9'
                    arr[n - 1 - i] = '9'
                    n_ex -= 2
        elif n_ex == 1:
            if i_diff < n_d and i == diff[i_diff]:
                if arr[i] != '9' and arr[n - 1 - i] != '9':
                    arr[i] = '9'
                    arr[n - 1 - i] = '9'
                    n_ex -= 1
                    # n_d -= 1
                else:
                    if int(arr[i]) > int(arr[n - 1 - i]):
                        arr[n - 1 - i] = arr[i]
                    else:
                        arr[i] = arr[n - 1 - i]
                i_diff += 1
        else: # ex_size == 0
            if i_diff < n_d and i == diff[i_diff]:
                if int(arr[i]) > int(arr[n - 1 -i]):
                    arr[n - 1 - i] = arr[i]
                else:
                    arr[i] = arr[n - 1 - i]
                i_diff += 1
    if n_ex >= 1 and n % 2 == 1:
        arr[n // 2] = '9'
        n_ex -= 1
    return ''.join(arr)

if __name__ == '__main__':
    s = '932239'
    n = 6
    k = 2
    print(highestValuePalindrome(s, n, k))