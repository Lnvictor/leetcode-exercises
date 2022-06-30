# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True

        return self.helper(root.left, root.right)

    def helper(self, a: TreeNode, b: TreeNode) -> bool:
        if a is None and b is None:
            return True
        if a is not None and b is not None and a.val == b.val:
            return (
                True and self.helper(a.left, b.right) and self.helper(a.right, b.left)
            )
        return False
