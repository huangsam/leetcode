// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import container.TreeNode;

public class KthSmallestBST {
    /**
     * We use a helper function to perform an in-order traversal of the BST.
     * The helper terminates when we reach the k-th smallest element.
     * This approach ensures we only traverse the tree as much as necessary.
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(h + k)</li>
     *     <li>Space: O(h)</li>
     * </ul>
     */
    public int kthSmallest(TreeNode root, int k) {
        Counter counter = new Counter();
        TreeNode result = helper(root, k, counter);
        return result.val;
    }

    /**
     * Helper function to perform in-order traversal.
     * It increments the current count and checks if it matches k.
     */
    private TreeNode helper(TreeNode root, int k, Counter counter) {
        if (root == null) {
            return null;
        }

        // Search left subtree first
        TreeNode left = helper(root.left, k, counter);
        if (left != null) {
            return left; // Found in left subtree
        }

        // Process current node
        counter.count++;
        if (counter.count == k) {
            return root;
        }

        // Search right subtree
        return helper(root.right, k, counter);
    }

    /**
     * Wrapper class to hold mutable counter state.
     */
    private static class Counter {
        int count = 0;
    }
}
