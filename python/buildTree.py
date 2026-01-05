# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from collections import deque
from typing import Deque, List, Optional

from container.binary_tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Build a binary tree from preorder and inorder traversal arrays.
        
        Complexity:
        - Time: O(n)
        - Space: O(n)
        """
        # Build index map for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        return self._build(deque(preorder), inorder, 0, len(inorder) - 1, inorder_map)

    def _build(self, prequeue: Deque[int], inorder: List[int], start: int, end: int, inorder_map: dict) -> Optional[TreeNode]:
        if start > end:
            return None

        # The first element in preorder is the root of the tree
        root_val = prequeue.popleft()
        root = TreeNode(root_val)
        idx = inorder_map[root_val]

        # Recursively build the left and right subtrees
        root.left = self._build(prequeue, inorder, start, idx - 1, inorder_map)
        root.right = self._build(prequeue, inorder, idx + 1, end, inorder_map)

        return root
