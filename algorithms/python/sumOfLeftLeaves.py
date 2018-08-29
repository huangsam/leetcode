# https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isLeafNode(self, root):
        return root.left is None and root.right is None

    def sumWorkhorse(self, root):
        if root is None:
            return 0
        elif self.isLeafNode(root):
            return root.val

        left_sum = self.sumWorkhorse(root.left)
        right_sum = self.sumWorkhorse(root.right)

        if root.right and self.isLeafNode(root.right):
            right_sum = 0

        return left_sum + right_sum

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or self.isLeafNode(root):
            return 0
        return self.sumWorkhorse(root)
