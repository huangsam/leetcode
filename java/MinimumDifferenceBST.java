// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

import container.TreeNode;

public class MinimumDifferenceBST {
    private TreeNode visited;

    public int getMinimumDifference(TreeNode root) {
        if (root == null) {
            return Integer.MAX_VALUE;
        }

        int leftResult = getMinimumDifference(root.left);

        int result = (visited != null) ? root.val - visited.val : Integer.MAX_VALUE;

        visited = root;

        int rightResult = getMinimumDifference(root.right);

        return (int) Math.min(Math.min(leftResult, result), rightResult);
    }
}
