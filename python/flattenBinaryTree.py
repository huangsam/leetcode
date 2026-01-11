# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten a binary tree to a linked list in-place.

        Recursively flatten left and right subtrees. Then, set root.right to the flattened left subtree.

        Find the end of the flattened left, set its right to the flattened right. Set root.left to None.

        Complexity:
        - Time: O(n)
        - Space: O(h)
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
