from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.hlp(root)
    
    def hlp(self, root, paths=None):
        if root is None:
            return 0
        
        if paths is None:
            paths = deque()
            paths.append([root.val])

        if root.left is None and root.right is None:
            return self.sum_of_paths(list(paths))

        l_paths = deque()
        r_paths = deque()

        for i in paths:
            l_paths.append(i.copy())
            r_paths.append(i.copy())

        result = 0
        if root.left is not None:
            l_paths[-1].append(root.left.val)
            result += self.hlp(root.left, paths=l_paths)
        if root.right is not None:
            r_paths[-1].append(root.right.val)
            result += self.hlp(root.right, paths=r_paths)

        return result
    
    def sum_of_paths(self, paths):
        if len(paths) == 1:
            if len(paths[0]) == 1:
                return paths[0][0]
        
        tot = 0
    
        for path in paths:
            for i in range(len(path)):
                tot += path[i] * (10 ** (len(path) - (i + 1)))

        return tot