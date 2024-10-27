// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import container.TreeNode;

public class KthSmallestBST {
    private TreeNode last = null;
    private int current = 0;

    public int kthSmallest(TreeNode root, int k) {
        try {
            helper(root, k);
        } catch (RuntimeException e) {
            return last.val;
        }
        return -1; // This should not happen!
    }

    private void helper(TreeNode root, int k) {
        if (root == null) {
            return;
        }

        helper(root.left, k);

        last = root;

        current += 1;

        // Unconditionally short-circuit with the kth node
        if (current == k) {
            throw new RuntimeException();
        }

        helper(root.right, k);
    }
}
