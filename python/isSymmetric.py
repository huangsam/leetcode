# https://leetcode.com/problems/symmetric-tree/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if a binary tree is symmetric around its center.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        if not root:
            raise ValueError("The input tree must have at least one node")
        return self._mirrorWorker(root.left, root.right)  # Check if left and right subtrees are mirrors

    def _mirrorWorker(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True  # Both null, symmetric
        elif not (left is not None and right is not None):
            return False  # One is null, the other isn't

        if not self._mirrorWorker(left.left, right.right):
            return False  # Left's left should match right's right
        elif not self._mirrorWorker(left.right, right.left):
            return False  # Left's right should match right's left

        if left.val != right.val:
            return False

        return True
