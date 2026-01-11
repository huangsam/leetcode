# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from container.binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Find the maximum depth of a binary tree.

        Use a recursive approach: if the root is None, return 0.
        Otherwise, recursively calculate the maximum depth of the left
        and right subtrees and return the greater one plus one.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        if root is None:
            return 0

        # Use post-order traversal to calculate the maximum depth
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)

        return max(left_depth, right_depth)
