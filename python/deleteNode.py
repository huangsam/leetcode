# https://leetcode.com/problems/delete-node-in-a-bst/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            # Recursively delete from the left subtree
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Recursively delete from the right subtree
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: find the in-order successor (smallest in the right subtree)
            min_node = self._findMin(root.right)

            # Replace current node's value with in-order successor's value
            root.val = min_node.val

            # Delete the in-order successor from the right subtree
            root.right = self.deleteNode(root.right, root.val)
        return root

    def _findMin(self, node):
        while node.left:
            node = node.left
        return node
