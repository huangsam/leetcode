# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from container.binary_tree import TreeNode


class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)
        max_depth = max(left_depth, right_depth)
        return max_depth
