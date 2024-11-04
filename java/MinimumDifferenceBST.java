// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

import container.TreeNode;

public class MinimumDifferenceBST {
    private TreeNode last = null;

    /**
     * We assume that the input is a binary search tree with at least two
     * nodes. Based on this, we can always assume there is a previous node
     * and a current node. As we perform inorder traversal, we can check
     * for the node that's being visited and see if there was a previously
     * visited node. If that node exists, we subtract the difference between
     * them, otherwise we return positive infinity. Then at the root node, we
     * collect the results from left and right sides, and get the minimum of
     * all results.
     */
    public int getMinimumDifference(TreeNode root) {
        if (root == null) {
            return Integer.MAX_VALUE;
        }

        int leftResult = getMinimumDifference(root.left);

        int result = (last != null) ? root.val - last.val : Integer.MAX_VALUE;

        last = root;

        int rightResult = getMinimumDifference(root.right);

        return Math.min(Math.min(leftResult, result), rightResult);
    }
}
