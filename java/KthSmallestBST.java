// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import container.TreeNode;

public class KthSmallestBST {
    private TreeNode last = null;
    private int current = 0;

    /**
     * We use a helper function to perform an in-order traversal of the BST.
     * The in-order traversal visits nodes in ascending order for a BST.
     * We keep track of the number of nodes visited so far using a counter.
     * When the counter reaches k, we set the last visited node as the result.
     * This approach ensures we only traverse the tree as much as necessary,
     */
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
