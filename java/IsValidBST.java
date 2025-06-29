// https://leetcode.com/problems/validate-binary-search-tree/

import container.TreeNode;

public class IsValidBST {
    private TreeNode last = null;

    /**
     * We process the answer recursively with in-order traversal. The idea is to
     * look for a previous entry if it exists and see if that entry is less than,
     * or equal to, the current entry.
     */
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        boolean isLeftValid = isValidBST(root.left);

        if (last != null && last.val >= root.val) {
            return false; // Flag any incoming contradictions
        }

        last = root;

        boolean isRightValid = isValidBST(root.right);

        return isLeftValid && isRightValid;
    }
}
