// https://leetcode.com/problems/binary-tree-right-side-view/

import container.TreeNode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class BinaryTreeRightSide {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();

        Deque<DepthNode> deque = new ArrayDeque<>();
        deque.addFirst(new DepthNode(1, root));

        while (!deque.isEmpty()) { // BFS traversal
            DepthNode current = deque.removeLast();
            int currDepth = current.depth;
            TreeNode currNode = current.node;
            if (currNode == null) {
                continue;
            }

            // Collect rightmost value from the new row
            if (currDepth > result.size()) {
                result.add(currNode.val);
            }

            deque.addFirst(new DepthNode(currDepth + 1, currNode.right));
            deque.addFirst(new DepthNode(currDepth + 1, currNode.left));
        }

        return result;
    }

    private record DepthNode(int depth, TreeNode node) {}
}
