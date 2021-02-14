class Solution:
    def countPrimes(self, n: int) -> int:
        notPrime = [False] * n
        count = 0
        for i in range(2, n):
            if notPrime[i] == False:
                count += 1
                for j in range(2, ((n - 1) // i) + 1):
                    notPrime[i * j] = True
        return count
