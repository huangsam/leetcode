# https://leetcode.com/problems/maximum-binary-tree/

from typing import List, Optional

from container.binary_tree import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """Construct maximum binary tree from array."""
        if not nums:
            return None

        # Find the maximum number and its index using built-in functions
        max_num = max(nums)
        max_ind = nums.index(max_num)

        # Create the root node with the maximum number
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_ind])
        root.right = self.constructMaximumBinaryTree(nums[max_ind + 1 :])

        return root
