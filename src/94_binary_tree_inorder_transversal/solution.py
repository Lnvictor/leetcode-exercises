# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque()
        output_arr = []

        if not root:
            return output_arr

        current_node = root

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            output_arr.append(current_node.val)
            current_node = current_node.right

        return output_arr
