# https://leetcode.com/problems/path-sum/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Determine if the tree has a root-to-leaf path with a given sum.

        Use a recursive approach: if the root is None, return false.
        Subtract the current node's value from targetSum and check if the
        left or right subtree has a path summing to the new targetSum. For
        leaf nodes, check if targetSum equals the node's value.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        # No node
        if not root:
            return False

        # Current node is leaf and has sum
        if not root.left and not root.right and targetSum == root.val:
            return True

        # Subtract before recursing further for the end result
        remainder = targetSum - root.val

        # The answer should be found in the children nodes
        return self.hasPathSum(root.left, remainder) or self.hasPathSum(root.right, remainder)
