# https://leetcode.com/problems/balanced-binary-tree/

from container.binary_tree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.nodeHeight(root) != -1

    def nodeHeight(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = self.nodeHeight(root.left)
        if left_height == -1:
            return -1
        right_height = self.nodeHeight(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
