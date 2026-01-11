# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree (mirror it).

        Use a recursive approach: if the root is None, return None. Otherwise, swap the left
        and right children, then recursively invert the left and right subtrees.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        if root is None:
            return None

        # Swap the left and right children
        if root.left or root.right:
            root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root
