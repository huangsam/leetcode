# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left) + 1
        right_depth = self.maxDepth(root.right) + 1
        return max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        return max(left_depth + right_depth, left_diameter, right_diameter)
