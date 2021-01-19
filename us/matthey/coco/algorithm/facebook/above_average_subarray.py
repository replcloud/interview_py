def aboveAverageSubarrays(A):
    ans = []
    total = sum(A)
    L = len(A)
    target = total // 2 + 1
    subtotal = 0
    for i in range(L):
        subtotal += A[i]
        if subtotal >= target:
            for j in range(i, L):
                ans.append([1, j + 1])
            break
    for k in range(L):
        subtotal -= A[k]
        for l in range(i + 1, L):
            subtotal += A[l]
            if subtotal >= target:
                for m in range(l, L):
                    ans.append([k + 2, m + 1])
                break
    return ans

if __name__ == '__main__':
    A = [3, 4, 2]
    print(aboveAverageSubarrays(A))