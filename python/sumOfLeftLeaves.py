# https://leetcode.com/problems/sum-of-left-leaves/

from container.binary_tree import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None or self._isLeafNode(root):
            return 0
        return self._sumWorkhorse(root)

    def _sumWorkhorse(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif self._isLeafNode(root):
            return root.val

        left_sum = self._sumWorkhorse(root.left)
        right_sum = self._sumWorkhorse(root.right)

        if root.right and self._isLeafNode(root.right):
            right_sum = 0  # Right leaves don't count

        return left_sum + right_sum

    def _isLeafNode(self, root: TreeNode) -> bool:
        return root.left is None and root.right is None
