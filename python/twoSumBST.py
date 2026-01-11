# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional, Set

from container.binary_tree import TreeNode


class Solution:
    def __init__(self) -> None:
        self.complement_set: Set[int] = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Find two numbers in a BST that add up to a target value.

        Like other two-sum problems, use a set to store complements of seen values.

        Traverse the tree in-order, for each node, check if k - node.val is in the set.
        If yes, return true. Else add node.val to set.

        Complexity:
        - Time: O(n)
        - Space: O(h)
        """
        if root is None:
            return False

        if self.findTarget(root.left, k):
            return True

        if root.val in self.complement_set:
            return True

        # If we haven't found a match, we add the complement
        self.complement_set.add(k - root.val)

        if self.findTarget(root.right, k):
            return True

        # If we reach here, we haven't found any two values that sum to k
        return False
