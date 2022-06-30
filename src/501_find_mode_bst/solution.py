from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not (root.left or root.right):
            return root.val

        frequency_mapping = {}

        self._resolve(root, frequency_mapping)
        sorted_frequency = {
            k: v for k, v in sorted(frequency_mapping.items(), key=lambda item: item[1])
        }

        resp = []

        for i in list(sorted_frequency.keys())[::-1]:
            if sorted_frequency[i] == list(sorted_frequency.values())[-1]:
                resp.append(i)

        return resp

    def _resolve(self, root, frequency_mapping):
        if root.val in frequency_mapping.keys():
            frequency_mapping[root.val] += 1
        else:
            frequency_mapping[root.val] = 1

        if root.left:
            self._resolve(root.left, frequency_mapping)
        if root.right:
            self._resolve(root.right, frequency_mapping)


if __name__ == "__main__":
    root = TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=2)))
    print(Solution().findMode(root))
