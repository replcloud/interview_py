from collections import defaultdict


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = defaultdict(dict)
        for i in range(m):
            if i == 0:
                for j in range(n):
                    matrix[i][j] = 1
            else:
                matrix[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]

        # def helper(x: int, y: int):
        #     if x == 0 or y == 0:
        #         return 1
        #     return helper(x - 1, y) + helper(x, y - 1)
        #
        # return helper(m - 1, n - 1)


if __name__ == '__main__':
    input = [3, 7]
    # input = [23, 12]
    print(Solution().uniquePaths(*input))
