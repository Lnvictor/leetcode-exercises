from tabnanny import check
from typing import Optional
from collections import deque, namedtuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        length = 1
        nodes = deque([(1, root)])

        while nodes:
            current_node = nodes.pop()[1]
            
            if not self.check_node(current_node):
                return current_node[0]

            length += 1

            if current_node.right:
                nodes.append((length, current_node.right))
            if current_node.left:
                nodes.append((length, current_node.left))

        return length



    def check_node(self, node: TreeNode) -> bool:
        return node.right or node.left

    
if __name__ == "__main__":
    root = TreeNode(
        val=3,
        left=TreeNode(
            val=1,
            left=TreeNode(
                val=0
            ),
            right=TreeNode(
                val=2
            )
        ),
        right=TreeNode(
            val=5,
            left=TreeNode(
                val=4,
                left=TreeNode(val=3)
            ),
            right=TreeNode(
                val=6,
            )
        )
    )
    Solution().minDepth(root)