# https://leetcode.com/problems/diameter-of-binary-tree/

from container.binary_tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """Calculate the diameter of a binary tree."""
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        return max(left_depth + right_depth, left_diameter, right_diameter)

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1
        return max(left_depth, right_depth)
