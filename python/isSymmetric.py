# https://leetcode.com/problems/symmetric-tree/
from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            raise ValueError("The input tree must have at least one node")
        return self.mirrorWorker(root.left, root.right)

    def mirrorWorker(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if l is None and r is None:
            return True
        elif not (l is not None and r is not None):
            return False

        if not self.mirrorWorker(l.left, r.right):
            return False
        elif not self.mirrorWorker(l.right, r.left):
            return False

        if l.val != r.val:
            return False

        return True
