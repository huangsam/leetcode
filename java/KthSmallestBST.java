// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import container.TreeNode;

public class KthSmallestBST {
    private TreeNode last = null;
    private int current = 0;

    public int kthSmallest(TreeNode root, int k) {
        helper(root, k);
        return last.val;
    }

    private void helper(TreeNode root, int k) {
        if (root == null) {
            return;
        }

        helper(root.left, k);

        current++;
        if (current == k) {
            last = root;
            return; // Early return to avoid unnecessary recursion
        }

        helper(root.right, k);
    }
}
