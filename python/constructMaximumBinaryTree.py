# https://leetcode.com/problems/maximum-binary-tree/
from typing import List

from container.binary_tree import TreeNode


class Solution(object):
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        max_num = None
        max_ind = None
        for ind, num in nums.items():
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
