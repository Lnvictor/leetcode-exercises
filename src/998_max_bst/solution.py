
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inserIntoMaxTree(self, root: Optional[TreeNode], val: int):
        final_list = self.build_array(root)
        max_n = max(final_list)
        if max_n < val:
            return TreeNode(val=val, left=self.constructMaximumBinaryTree(final_list))
        else:
            final_list.append(val)
        return self.constructMaximumBinaryTree(final_list)

    def build_array(self, root: TreeNode):
        output_array = [root.val]
        curr_node = root
        stack = deque()

        while curr_node or stack:
            index = output_array.index(curr_node.val)
            if curr_node.right:
                output_array.insert(index + 1, curr_node.right.val)
                stack.append(curr_node.right)
            if curr_node.left:
                output_array.insert(index, curr_node.left.val)
                stack.append(curr_node.left)
            try:
                curr_node = stack.pop()
            except Exception:
                break

        return output_array

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_nums = max(nums)
        root = TreeNode(val=max_nums)
        root.left = self.constructMaximumBinaryTree(nums[0:nums.index(max_nums)])
        root.right = self.constructMaximumBinaryTree(nums[nums.index(max_nums) + 1:])

        return root


if __name__ == '__main__':
    # TestCases
    s = Solution()
    root = TreeNode(val=5, left=TreeNode(val=4, left=TreeNode(val=1), right=TreeNode(val=2)))
    print(s.inserIntoMaxTree(root, 5))
