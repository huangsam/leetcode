# https://leetcode.com/problems/symmetric-tree/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Check if a binary tree is symmetric around its center.
        
        A tree is symmetric if its left and right subtrees are mirror images of each other.
        """
        if not root:
            raise ValueError("The input tree must have at least one node")
        return self._mirrorWorker(root.left, root.right)

    def _mirrorWorker(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """Recursively check if two subtrees are mirror images of each other."""
        # Both subtrees are empty - they're symmetric
        if left is None and right is None:
            return True
        # One subtree is empty but not the other - not symmetric
        elif not (left is not None and right is not None):
            return False

        # Recursively check outer nodes (left.left vs right.right)
        if not self._mirrorWorker(left.left, right.right):
            return False
        # Recursively check inner nodes (left.right vs right.left)
        elif not self._mirrorWorker(left.right, right.left):
            return False

        # Check if current node values match
        if left.val != right.val:
            return False

        return True
