# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        max_num = None
        max_ind = None
        for ind, num in enumerate(nums):
            if max_num is None and max_ind is None:
                max_num = num
                max_ind = ind
            elif max_num < num:
                max_num = num
                max_ind = ind
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_ind])
        root.right = self.constructMaximumBinaryTree(nums[(max_ind + 1) :])
        return root
