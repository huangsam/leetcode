# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check base cases for similar structure
        if not p and not q:
            return True
        elif p and not q:
            return False
        elif q and not p:
            return False

        # Check answers from the bottom
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)
        if not left_same or not right_same:
            return False

        # Check for similar value between both nodes
        if p.val != q.val:
            return False

        return True
