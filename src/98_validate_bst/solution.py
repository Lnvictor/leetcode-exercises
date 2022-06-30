from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if root.right and root.val >= root.right.val:
            return False

        if root.left and root.val <= root.left.val:
            return False

        return self._resolve(root.left, [root], "L") and self._resolve(
            root.right, [root], "R"
        )

    def _resolve(self, root: TreeNode, grandfathers: List[TreeNode], flag: str):
        if not root:
            return True

        grandfather = min(grandfathers, key=lambda x: x.val)

        if root.left and root.left.val >= root.val:
            return False

        if root.right and root.right.val <= root.val:
            return False

        if (
            flag == "L"
            and (root.right and root.right.val >= grandfather.val)
            or (
                root.left
                and grandfather.val != root.val
                and grandfather.val <= root.left.val
            )
        ):
            return False

        if (
            flag == "R"
            and (root.left and root.left.val <= grandfather.val)
            or (
                root.right
                and grandfather.val != root.val
                and grandfather.val >= root.right.val
            )
        ):
            return False

        grandfathers.append(root)

        return self._resolve(root.left, grandfathers, "L") and self._resolve(
            root.right, grandfathers, "R"
        )


if __name__ == "__main__":
    # [120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]
    # root = TreeNode(
    #     val=120,
    #     left=TreeNode(
    #         val=70,
    #         left=TreeNode(
    #             val=50,
    #             left=TreeNode(val=20),
    #             right=TreeNode(val=55)
    #         ),
    #         right=TreeNode(
    #             val=100,
    #             left=TreeNode(val=75),
    #             right=TreeNode(val=110)
    #         )
    #     ),
    #     right=TreeNode(
    #         val=140,
    #         left=TreeNode(
    #             val=130,
    #             left=TreeNode(val=119),
    #             right=TreeNode(val=135)
    #         ),
    #         right=TreeNode(
    #             val=160,
    #             left=TreeNode(val=150),
    #             right=TreeNode(val=200)
    #         )
    #     )
    # )

    # [3,1,5,0,2,4,6,null,null,null,3]
    root = TreeNode(
        val=3,
        left=TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=2)),
        right=TreeNode(
            val=5,
            left=TreeNode(val=4, left=TreeNode(val=3)),
            right=TreeNode(
                val=6,
            ),
        ),
    )

    print(Solution().isValidBST(root))
