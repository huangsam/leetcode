# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        if root.left is None:
            self.flatten(root.right)
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left, right = root.left, root.right

        # We no longer want any nodes on left side
        root.left = None

        # We want all nodes on the right side
        root.right = left

        # Traverse until we hit the tail of the right side
        curr = root.right
        while curr.right is not None:
            curr = curr.right

        # Connect the left.tail with the right.head
        curr.right = right
