from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def searchHelper( low, high) -> int:
            i = low
            j = high
            if i <= j:

                m = (i + j) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    return searchHelper(m + 1, high)
                else:
                    return searchHelper(low, m - 1)
            return -1

        return searchHelper(0, len(nums)-1)

    def search2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

if __name__ == '__main__':
    print(Solution().search([-1,0,3,5,9,12], 13))
