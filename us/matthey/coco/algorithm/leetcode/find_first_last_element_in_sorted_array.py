from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        h = len(nums) - 1
        m = l + (h - l) // 2
        s = -1
        e = -1
        while (l <= h):
            if nums[m] == target:
                s = m
                e = m
                while s > 0 and nums[s - 1] == target:
                    s -= 1
                while e < len(nums) - 1 and nums[e + 1] == target:
                    e += 1
                break
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
            m = l + (h - l) // 2
        return [s, e]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    nums = [1]
    target = 1
    print(Solution().searchRange(nums, target))
