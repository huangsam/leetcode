# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from container.binary_tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
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
