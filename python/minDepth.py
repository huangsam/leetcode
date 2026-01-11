# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from container.binary_tree import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        Find the minimum depth of a binary tree.

        Recursively calculate: if root is None, return 0. Compute left and right depths.

        If one is 0 (empty subtree), return the other +1. Else, return min(left, right) +1.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        if root is None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0:
            return right_depth + 1
        elif right_depth == 0:
            return left_depth + 1
        return min(left_depth, right_depth) + 1
