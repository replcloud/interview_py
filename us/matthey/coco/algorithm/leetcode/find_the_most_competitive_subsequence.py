from typing import List


class Solution:
    def mostCompetitiveFactorial(self, nums: List[int], k: int) -> List[int]:
        res = []
        start = 0
        N = len(nums)
        for i in range(k):
            sml = min(nums[start:N + i - k + 1])
            start = nums.index(sml, start, N + i - k + 1) + 1
            res.append(sml)
        return res

    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        attempts = len(nums) - k
        stack = []
        for num in nums:
            while stack and nums < stack[-1] and attempts > 0:
                stack.pop()
                attempts -= 1
            stack.append(num)
        return stack[:k]


if __name__ == '__main__':
    nums = [2, 4, 3, 3, 5, 4, 9, 6]
    k = 4
    print((Solution().mostCompetitive(nums, k)))
