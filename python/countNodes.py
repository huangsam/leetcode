# https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional

from container.binary_tree import TreeNode


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Count the number of nodes in a complete binary tree.

        Figure out height of left and right hand side.
        If they are equal then you can stop. Otherwise, you
        continue traversing the left and right subtrees, both
        of which are complete trees.

        Complexity:
        - Time: O(log^2(n))
        - Space: O(log(n))
        """
        if not root:
            return 0

        left_height, right_height = 1, 1
        left, right = root, root

        while left := left.left:
            left_height += 1

        while right := right.right:
            right_height += 1

        # We are done if we see a full tree
        if left_height == right_height:
            return 2**left_height - 1

        # Process left complete subtree and right complete subtree
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
