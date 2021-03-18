class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [False, False] + [True] * (n-2)
        for p in range(2, int(n**0.5) + 1):
            if isPrime[p]:
                for i in range(2*p, n, p):
                    isPrime[i] = False
        return isPrime.count(True)

if __name__ == '__main__':
    print(Solution().countPrimes(10))