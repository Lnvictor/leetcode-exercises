# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 1
        
        if root == None:
            return 0
        
        if root.left is not None and root.right is not None:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        if root.left is None and root.right is not None:
            return 1 +self.maxDepth(root.right)
        return 1 + self.maxDepth(root.left)
        