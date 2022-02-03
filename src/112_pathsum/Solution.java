/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
    
        if (root == null) return false;
        TreeNode left = root.left;
        TreeNode right = root.right;
        
        if (left == null && right == null){
            return root.val == sum;
        }
        
        
        boolean pathL = false;
        boolean pathR = false;
        
        if (left != null){
            pathL= hasPathSum(left, sum - root.val); 
        }
        
        if (right != null){
            pathR = hasPathSum(right, sum - root.val);
        }
        
        
        return  pathL || pathR;
    }
}