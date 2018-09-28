# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
