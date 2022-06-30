# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.max_depth(root) is not None

    def max_depth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_side = self.max_depth(root.left)
        right_side = self.max_depth(root.right)

        if left_side is None or right_side is None:
            return None

        if abs(left_side - right_side) > 1:
            return None

        return max(left_side, right_side) + 1
