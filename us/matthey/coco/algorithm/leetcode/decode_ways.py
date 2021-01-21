class Solution:
    def numDecodings(self, s: str) -> int:
        CODE = [str(i) for i in range(1, 27)]
        N = len(s)
        dp = [1] + [0] * N
        if len(s) == 0: return 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, N + 1):
            first = s[i - 1:i]
            second = s[i - 2:i]
            if first in CODE:
                dp[i] += dp[i - 1]
            if second in CODE:
                dp[i] += dp[i - 2]
        return dp[N]


if __name__ == '__main__':
    # s = "111111111111111111111111111111111111111111111"
    s = "12"
        # s = "226"
        # s = "0"
        # s = "1"
    print(Solution().numDecodings(s))
