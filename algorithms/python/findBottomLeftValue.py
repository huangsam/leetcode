# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leftmost_value = root.val
        to_visit = [root]

        while len(to_visit) > 0:
            node = to_visit.pop(0)
            if node.right:
                to_visit.append(node.right)
            if node.left:
                to_visit.append(node.left)
            leftmost_value = node.val
        return leftmost_value
