# https://leetcode.com/problems/path-sum/
from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # No node
        if not root:
            return False

        # Current node is leaf and has sum
        if not root.left and not root.right and targetSum == root.val:
            return True

        # Subtract before recursing further for the end result
        remainder = targetSum - root.val

        # The answer should be found in the children nodes
        return (
            self.hasPathSum(root.left, remainder)
            or
            self.hasPathSum(root.right, remainder)
        )
