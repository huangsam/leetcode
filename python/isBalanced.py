# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._nodeHeight(root) != -1

    def _nodeHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height = self._nodeHeight(root.left)
        if left_height == -1:
            return -1
        right_height = self._nodeHeight(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
