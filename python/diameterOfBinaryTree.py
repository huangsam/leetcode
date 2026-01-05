# https://leetcode.com/problems/diameter-of-binary-tree/

from container.binary_tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Complexity:
        - Time: O(n)
        - Space: O(h)

        Calculate the diameter of a binary tree.
        """
        self.diameter = 0

        def depth(node: TreeNode) -> int:
            """Calculate depth and update diameter in one traversal."""
            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update diameter if path through this node is longer
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return depth of this subtree
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.diameter
