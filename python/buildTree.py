# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from collections import deque
from typing import Deque, List, Optional

from container.binary_tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self._build(deque(preorder), inorder)

    def _build(self, prequeue: Deque[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        # The first element in preorder is the root of the tree
        idx = inorder.index(prequeue.popleft())
        root = TreeNode(inorder[idx])

        # Recursively build the left subtree
        root.left = self._build(prequeue, inorder[:idx])

        # Recursively build the right subtree
        root.right = self._build(prequeue, inorder[idx + 1 :])

        return root
