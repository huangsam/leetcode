# https://leetcode.com/problems/symmetric-tree/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            raise ValueError("The input tree must have at least one node")
        return self._mirrorWorker(root.left, root.right)

    def _mirrorWorker(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif not (left is not None and right is not None):
            return False

        if not self._mirrorWorker(left.left, right.right):
            return False
        elif not self._mirrorWorker(left.right, right.left):
            return False

        if left.val != right.val:
            return False

        return True
