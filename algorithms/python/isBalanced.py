# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def nodeHeight(self, root):
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

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.nodeHeight(root) != -1
