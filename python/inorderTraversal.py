# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import List

from container.binary_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Perform inorder traversal of a binary tree.

        Recursively visit left subtree, then append root value, then visit right subtree.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        if root is None:
            return []

        # Classic recursive solution
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))

        return result

    def inorderTraversalIterative(self, root: TreeNode) -> List[int]:
        """
        Perform inorder traversal of a binary tree using an iterative approach.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        visited: List[int] = []
        c = root
        s = []

        while c is not None or len(s) > 0:
            # Keep going left
            while c is not None:
                s.append(c)
                c = c.left

            # Visit current node
            c = s.pop()
            visited.append(c.val)

            # Go to next node to the right
            c = c.right

        return visited
