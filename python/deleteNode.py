# https://leetcode.com/problems/delete-node-in-a-bst/


from python.model.binary_tree import TreeNode


class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        """
        Delete a node in a BST.

        Recursively search for the node with the key. If found:

        - If no children, return None.
        - If one child, return the child.
        - If two children, replace value with in-order successor and remove it in one pass.

        Complexity:
        - Time: O(h)
        - Space: O(h)
        """
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

            # Two children: find successor value and remove it in a single pass
            root.right, root.val = self._deleteMin(root.right)
        return root

    def _deleteMin(self, node: TreeNode) -> tuple[TreeNode | None, int]:
        """Remove the minimum node from subtree in one pass.

        Returns (modified subtree root, min value).
        """
        if node.left is None:
            return node.right, node.val
        node.left, min_val = self._deleteMin(node.left)
        return node, min_val
