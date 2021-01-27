from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        if index < len(self.nums):
            self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        def helper(self, left, right):
            if right - left == 1:
                total += self.nums[left] + self.nums[right]
            elif right - left == 0:
                total += self.nums[left]
            else:
                m = left + (right - left) // 2
                total += helper(self, left, m)
                total += helper(self, m + 1, right)
        helper(self, left, right)
        # for i in range(left, right + 1):
        #     total += self.nums[i]
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [2, 3]]
    obj = NumArray([[1, 3, 5]])
    print(obj.sumRange(0, 2))
    obj.update(1, 2)
    print(obj.sumRange(0, 2))
