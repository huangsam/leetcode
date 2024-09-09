# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # No node
        if not root:
            return False

        # Current node is leaf and has sum
        if not root.left and not root.right and targetSum == root.val:
            return True

        # Subtract before recursing further for the end result
        remainder = targetSum - root.val

        # The answer should be found in the children nodes
        return (
            self.hasPathSum(root.left, remainder)
            or
            self.hasPathSum(root.right, remainder)
        )
