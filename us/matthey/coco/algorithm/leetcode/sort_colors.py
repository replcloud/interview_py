from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        L = len(nums)
        end = L - 1
        i = 0
        while i <= end:
            if i > end: break
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
        return nums

if __name__ == '__main__':
    input = [2,0,2,1,1,0]
    Solution().sortColors(input)
    print(input)