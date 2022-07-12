from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()
        my_stack = deque()

        current_node = root

        while current_node or stack:
            while current_node:
                stack.appendleft(current_node)
                current_node = current_node.left

            current_node = stack.popleft()
            my_stack.append(current_node.val)
            current_node = current_node.right

        counter = 0
        while counter < k:
            current_node = my_stack.popleft()
            counter += 1

        return current_node


# TestCases
if __name__ == '__main__':
    root = TreeNode(val=5, left=TreeNode(
                                val=3,
                                left=TreeNode(val=2, left=TreeNode(val=1)),
                                right=TreeNode(val=4)),
                    right=TreeNode(val=6))

    s = Solution()
    print(s.kthSmallest(root, 3))
