from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        smax = nums[0]
        ssum = 0
        smin = 0
        for x in nums:
            ssum += x
            if smax < ssum - smin:
                smax = ssum - smin
            if smin > ssum:
                smin = ssum
        return smax

if __name__ == '__main__':
    l = [-2, -1]
    print(Solution().maxSubArray(l))