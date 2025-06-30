# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional, Set

from container.binary_tree import TreeNode


class Solution:
    def __init__(self) -> None:
        self.complement_set: Set[int] = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Like other two-sum problems, we can use a cache to store
        the complements of the values we have seen so far. The
        complement is the value we need to find in order to reach
        the target sum `k`. We traverse the tree in-order, checking
        if the current node's value is in the complement set.
        If it is, we have found two values that sum to `k`.
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
