from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_nums = max(nums)
        root = TreeNode(val=max_nums)
        root.left = self.constructMaximumBinaryTree(nums[0:nums.index(max_nums)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max_nums) + 1:])

        return root
