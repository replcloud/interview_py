from collections import deque
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = deque([[], [nums[-1]]])
        nums.pop()
        while len(nums) > 0:
            e = nums.pop()
            for i in range(len(q)):
                q.append(q[i] + [e])
        return q

        # if len(nums) == 1: return nums
        # fst = nums[0]
        # right = self.subsets(nums[1:])
        # res = []
        # for x in right:
        #     res.append([x] + [fst])
        # res += right
        #
        # return res

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().subsets(nums))