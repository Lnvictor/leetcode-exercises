/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<int> PreorderTraversal(TreeNode root) {
        Stack<TreeNode> toBeVisited = new Stack<TreeNode>();
        List<int> resp = new List<int>();

        if (root != null)
        {
            toBeVisited.Push(root);
        }

        while (toBeVisited.Count != 0)
        {
            TreeNode currentNode = toBeVisited.Pop();
            resp.Add(currentNode.val);
            TreeNode leftNode = currentNode.left;

            if (currentNode.right != null)
            {
                toBeVisited.Push(currentNode.right);
            }

            while (leftNode != null)
            {
                resp.Add(leftNode.val);

                if (leftNode.right != null)
                {
                    toBeVisited.Push(leftNode.right);
                }

                leftNode = leftNode.left;
            }
        }

        return resp;
    }
}