# https://leetcode.com/problems/find-bottom-left-tree-value/

from container.binary_tree import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        Time: O(n)
        Space: O(w)
        """
        leftmost_value = root.val
        to_visit = [root]

        # We will use a queue to perform a level order traversal
        while len(to_visit) > 0:
            node = to_visit.pop(0)
            if node.right:
                to_visit.append(node.right)
            if node.left:
                to_visit.append(node.left)
            leftmost_value = node.val

        return leftmost_value
