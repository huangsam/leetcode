// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import container.TreeNode;

public class KthSmallestBST {
    private TreeNode last = null;
    private int current = 0;

    /**
     * We use a helper function to perform an in-order traversal of the BST.
     * The helper terminates when we reach the k-th smallest element.
     * This approach ensures we only traverse the tree as much as necessary,
     */
    public int kthSmallest(TreeNode root, int k) {
        helper(root, k);
        return last.val;
    }

    /**
     * Helper function to perform in-order traversal.
     * It increments the current count and checks if it matches k.
     * If it does, it sets the last node to the current node.
     */
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
