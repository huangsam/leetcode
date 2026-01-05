# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if a binary tree is height-balanced.
        
        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        return self._nodeHeight(root) != -1

    def _nodeHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # Calculate the height of the left and right subtrees
        left_height = self._nodeHeight(root.left)
        right_height = self._nodeHeight(root.right)

        # Case 1: Either subtree is unbalanced
        if left_height == -1 or right_height == -1:
            return -1
        # Case 2: The current node is unbalanced
        elif abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
