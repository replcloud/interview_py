def solution(A):
    # write your code in Python 3.6
    unique_positive_A = set([x for x in A if x > 0])
    sorted_A = sorted(list(unique_positive_A))
    if len(sorted_A) == 0:
        return 1
    for i in range(len(sorted_A)):
        if sorted_A[i] != i + 1:
            return i + 1
    return len(sorted_A) + 1
