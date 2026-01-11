# https://leetcode.com/problems/same-tree/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determine if two binary trees are identical.

        Use a recursive approach: both trees are the same if both are None, or both
        are not None, have the same value, and their left and right subtrees
        are identical.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        # Check base cases for similar structure
        if p is None and q is None:
            return True
        elif not (p is not None and q is not None):
            return False

        # Check answers from the bottom
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        if not left_same or not right_same:
            return False

        # Check for similar value between both nodes
        if p.val != q.val:
            return False

        return True
