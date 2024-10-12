# https://leetcode.com/problems/maximum-binary-tree/

from typing import List, Optional

from container.binary_tree import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
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
        if isinstance(max_ind, int):
            root.left = self.constructMaximumBinaryTree(nums[:max_ind])
            root.right = self.constructMaximumBinaryTree(nums[(max_ind + 1) :])
        return root
