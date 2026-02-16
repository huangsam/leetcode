// https://leetcode.com/problems/validate-binary-search-tree/

import container.TreeNode;

public class IsValidBST {
    /**
     * Check if a binary tree is a valid binary search tree (BST).
     *
     * <p>We process the answer recursively with in-order traversal. The idea is to
     * look for a previous entry if it exists and see if that entry is less than,
     * or equal to, the current entry.
     *
     * <p>Complexity:
     *
     * <ul>
     *     <li>Time: O(n)</li>
     *     <li>Space: O(h)</li>
     * </ul>
     */
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, null, null);
    }

    /**
     * Helper method that validates BST property with min and max bounds.
     * @param node Current node being validated
     * @param min Minimum allowed value (exclusive)
     * @param max Maximum allowed value (exclusive)
     */
    private boolean isValidBST(TreeNode node, Integer min, Integer max) {
        if (node == null) {
            return true;
        }

        // Check if current node violates BST property
        if ((min != null && node.val <= min) || (max != null && node.val >= max)) {
            return false;
        }

        // Recursively validate left and right subtrees with updated bounds
        return isValidBST(node.left, min, node.val)
            && isValidBST(node.right, node.val, max);
    }
}
