# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return

        my_stack = []
        my_stack.append(root)

        while len(my_stack) > 0:
            curr_node = my_stack.pop()

            if curr_node.right is not None:
                my_stack.append(curr_node.right)

            if curr_node.left is not None:
                my_stack.append(curr_node.left)

            if len(my_stack) > 0:
                curr_node.right = my_stack[-1]

            curr_node.left = None
