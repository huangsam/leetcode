// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

import container.TreeNode;

public class MinimumDifferenceBST {
    /**
     * Time: O(n)
     * Space: O(h)
     *
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
        MinTracker tracker = new MinTracker();
        helper(root, tracker);
        return tracker.minDiff;
    }

    /**
     * Helper method for in-order traversal.
     */
    private void helper(TreeNode node, MinTracker tracker) {
        if (node == null) {
            return;
        }

        helper(node.left, tracker);

        if (tracker.prev != null) {
            tracker.minDiff = Math.min(tracker.minDiff, node.val - tracker.prev.val);
        }
        tracker.prev = node;

        helper(node.right, tracker);
    }

    /**
     * Wrapper class to track minimum difference and previous node during traversal.
     */
    private static class MinTracker {
        TreeNode prev = null;
        int minDiff = Integer.MAX_VALUE;
    }
}
