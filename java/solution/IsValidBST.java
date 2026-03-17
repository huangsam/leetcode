// https://leetcode.com/problems/validate-binary-search-tree/

package solution;

import java.util.ArrayDeque;
import java.util.Deque;

import model.TreeNode;

public class IsValidBST {
    /**
     * Check if a binary tree is a valid binary search tree (BST).
     *
     * <p>We use a pre-order traversal approach, where we maintain a range (min and max)
     * for each node. For the left child, the max is updated to the current node's
     * value, and for the right child, the min is updated to the current node's value.
     * If any node violates these bounds, we return false.
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

    /**
     * Check if a binary tree is a valid binary search tree (BST).
     *
     * <p>We process the answer iteratively with in-order traversal. In a valid
     * BST, the in-order traversal should yield values in strictly increasing
     * order. We use a stack to simulate the recursion and keep track of the
     * last visited node to compare values.
     */
    public boolean isValidBSTStack(TreeNode root) {
        if (root == null) { return true; }

        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode curr = root;
        TreeNode lastVisited = null;

        while (curr != null || !stack.isEmpty()) {
            // 1. Reach the leftmost node of the current subtree
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }

            // 2. Process the node
            curr = stack.pop();

            // Check BST property: Current must be strictly greater than last
            if (lastVisited != null && curr.val <= lastVisited.val) {
                return false;
            }
            lastVisited = curr;

            // 3. Now move to the right child
            curr = curr.right;
        }

        return true;
    }
}
