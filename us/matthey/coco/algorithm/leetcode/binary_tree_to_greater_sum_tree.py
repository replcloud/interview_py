# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    greater_sum = 0
    val = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # right = 0
        # print("val before " + str(root.val))
        # if root.right:
        #     right = self.bstToGst(root.right)
        # print("val " + str(root.val))
        # if root.left:
        #     self.bstToGst(root.left)
        # return root.val + right

        if root.right: self.bstToGst(root.right)
        print('self ' + str(self.val))
        root.val = self.val = self.val + root.val
        print('root ' + str(root.val))
        if root.left: self.bstToGst(root.left)
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    Solution().bstToGst(root)
