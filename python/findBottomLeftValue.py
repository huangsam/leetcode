# https://leetcode.com/problems/find-bottom-left-tree-value/

from collections import deque

from python.model.binary_tree import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        Find the leftmost value in the last row of a binary tree.

        Use level-order traversal with a queue. For each level, the first node
        dequeued is the leftmost.

        Update the result with this value at the start of each level, so the last
        update is for the bottom level.

        Complexity:
        - Time: O(n)
        - Space: O(w)
        """
        leftmost_value = root.val
        to_visit = deque([root])

        # We will use a queue to perform a level order traversal
        while to_visit:
            node = to_visit.popleft()
            if node.right:
                to_visit.append(node.right)
            if node.left:
                to_visit.append(node.left)
            leftmost_value = node.val

        return leftmost_value
