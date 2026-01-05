// https://leetcode.com/problems/average-of-levels-in-binary-tree/

import container.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class LevelAverage {
    /**
     * This method calculates the average value of nodes at each level in a binary tree.
     * Once the tree is traversed, it computes the average for each level
     * by dividing the total sum of node values at that level by the count of nodes.
     *
     * <p>Complexity:
     * <ul>
     *     <li>Time: O(n)</li>
     *     <li>Space: O(w)</li>
     * </ul>
     */
    public List<Double> averageOfLevels(TreeNode root) {
        List<SumCount> depthList = new ArrayList<>();
        helper(root, 0, depthList);
        return depthList.stream()
            .map(sc -> sc.sum() / sc.count())
            .toList();
    }

    /**
     * Helper function to traverse the tree and calculate the sum and count
     * of nodes at each depth. It uses a depth-first search approach.
     */
    private void helper(TreeNode root, int depth, List<SumCount> depthList) {
        if (root == null) {
            return;
        }
        if (depth > depthList.size() - 1) {
            depthList.add(new SumCount(0.0, 0.0));
        }
        SumCount sc = depthList.get(depth);
        depthList.set(
            depth,
            new SumCount(sc.sum + (double) root.val, sc.count + 1.0)
        );
        helper(root.left, depth + 1, depthList);
        helper(root.right, depth + 1, depthList);
    }

    private record SumCount(double sum, double count) {}
}
