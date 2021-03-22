class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [False, False] + [True] * (n-2)
        for p in range(2, int(n**0.5) + 1):
            if isPrime[p]:
                isPrime[2*p:n:p] = [False] * (((n - 1 - p) // p))
        return isPrime.count(True)

if __name__ == '__main__':
    print(Solution().countPrimes(10))