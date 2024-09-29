# https://leetcode.com/problems/find-bottom-left-tree-value/
from container.binary_tree import TreeNode


class Solution(object):
    def findBottomLeftValue(self, root: TreeNode) -> int:
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
