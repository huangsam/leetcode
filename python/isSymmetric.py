# https://leetcode.com/problems/symmetric-tree/
from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirrorWorker(root.left, root.right)

    def mirrorWorker(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if not l and not r:
            return True
        elif l and not r:
            return False
        elif r and not l:
            return False

        if not self.mirrorWorker(l.left, r.right):
            return False
        elif not self.mirrorWorker(l.right, r.left):
            return False

        if l.val != r.val:
            return False

        return True
