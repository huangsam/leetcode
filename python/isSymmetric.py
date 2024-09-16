# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirrorWorker(root.left, root.right)

    def mirrorWorker(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if not l and not r:
            return True
        elif l and not r:
            return False
        elif r and not l:
            return False

        if not self.mirrorWorker(l.left, r.right):
            return False
        elif not self.mirrorWorker(l.right, r.left):
            return False

        if l.val != r.val:
            return False

        return True
