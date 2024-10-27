// https://leetcode.com/problems/validate-binary-search-tree/

import container.TreeNode;

public class IsValidBST {
    private TreeNode last = null;

    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        boolean isLeftValid = isValidBST(root.left);

        if (last != null && last.val >= root.val) {
            return false;
        }

        last = root;

        boolean isRightValid = isValidBST(root.right);

        return isLeftValid && isRightValid;
    }
}
