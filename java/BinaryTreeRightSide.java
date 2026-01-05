// https://leetcode.com/problems/binary-tree-right-side-view/

import container.TreeNode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class BinaryTreeRightSide {
    /**
     * Time: O(n)
     * Space: O(h)
     *
     * Returns a list of integers representing the values of the nodes visible
     * from the right side of a binary tree when viewed from top to bottom.
     * <p> This method performs a breadth-first search (BFS) traversal of the binary
     * tree, ensuring that the rightmost node at each depth is added to the result.
     */
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        Deque<DepthNode> deque = new ArrayDeque<>();
        deque.addFirst(new DepthNode(1, root));

        while (!deque.isEmpty()) { // BFS traversal
            DepthNode current = deque.removeLast();
            if (current.node == null) {
                continue;
            }

            // Collect rightmost value from the new row
            if (current.depth > result.size()) {
                result.add(current.node.val);
            }

            deque.addFirst(new DepthNode(current.depth + 1, current.node.right));
            deque.addFirst(new DepthNode(current.depth + 1, current.node.left));
        }

        return result;
    }

    private record DepthNode(int depth, TreeNode node) {
    }
}
