# https://leetcode.com/problems/diameter-of-binary-tree/

from container.binary_tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Calculate the diameter of a binary tree."""
        if root is None:
            return 0

        # The diameter is the maximum of the following:
        # 1. The diameter of the left subtree
        # 2. The diameter of the right subtree
        # 3. The longest path through the root from left to right
        left_depth = self._maxDepth(root.left)
        right_depth = self._maxDepth(root.right)
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        return max(left_depth + right_depth, left_diameter, right_diameter)

    def _maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = self._maxDepth(root.left) + 1
        right_depth = self._maxDepth(root.right) + 1
        return max(left_depth, right_depth)
