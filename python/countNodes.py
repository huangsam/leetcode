# https://leetcode.com/problems/count-complete-tree-nodes/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Figure out height of left and right hand side.

        If they are equal then you can stop. Otherwise, you
        continue traversing the left and right subtrees, all
        of which are complete trees.
        """
        if not root:
            return 0

        left_height, right_height = 1, 1
        left, right = root, root

        while left := left.left:
            left_height += 1

        while right := right.right:
            right_height += 1

        # We are done if we see a full tree
        if left_height == right_height:
            return 2**left_height - 1

        # Process left complete subtree and right complete subtree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
